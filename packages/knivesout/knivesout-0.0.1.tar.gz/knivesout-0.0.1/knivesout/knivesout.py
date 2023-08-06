#!/usr/bin/env python3
import ast
import asyncio
import json
import os
import subprocess
import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf
import fire
import pandas as pd
from codefast.asyncio import async_render
from codefast.io.osdb import osdb
from codefast.logger import setpath
from pydantic import BaseModel
from rich import print

setpath('/var/log/knivesout.log')

_db = osdb('/var/log/knivesout.db')


class _ProgramState(object):
    running = 'running'
    stopped = 'stopped'
    error = 'error'
    init = 'init'


class Config(BaseModel):
    program: str
    directory: str
    command: str
    stdout_file: Optional[str] = '/tmp/stdout.txt'
    stderr_file: Optional[str] = '/tmp/stderr.txt'
    max_restart: Optional[int] = 3
    cur_restart: Optional[int] = 0
    cur_state: Optional[str] = ''
    next_state: Optional[str] = ''
    start_time: Optional[str] = pd.Timestamp.now().strftime(
        '%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return str(self.dict())

    def __eq__(self, other):
        return self.program == other.program and self.directory == other.directory and self.command == other.command

    def __hash__(self):
        return hash(self.program + self.directory + self.command)


def parse_config_from_file(config_file: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    js = cf.js(config_file)
    return Config(**js)


def parse_config_from_string(config_string: str) -> Config:
    """Parse config file and return a dictionary of parameters."""
    import ast
    try:
        js = ast.literal_eval(config_string)
        return Config(**js)
    except Exception as e:
        cf.error({
            'msg': 'parse_config_from_string error',
            'config_string': config_string,
            'error': str(e)
        })
        return None


class ConfigManager(object):

    @staticmethod
    def load() -> List[Config]:
        configs = _db.get('configs') or '[]'
        configs = [Config(**c) for c in ast.literal_eval(configs)]
        return list(set(configs))

    @staticmethod
    def add(config: Config):
        configs = ConfigManager.load()
        configs = [c for c in configs if c != config]
        configs.append(config)
        ConfigManager.save(configs)

    @staticmethod
    def stop_by_program_name(name: str):
        configs = ConfigManager.load()
        configs_new = []
        command = ''
        for c in configs:
            if c.program == name:
                c.next_state = _ProgramState.stopped
                c.cur_state = _ProgramState.running  # Give control to RunningSwitcher
                c.start_time = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
                command = c.command
            configs_new.append(c)
        ConfigManager.save(configs_new)
        return command

    @staticmethod
    def save(configs: List[Config]):
        configs = list(set(configs))
        configs = [c.dict() for c in configs]
        _db.set('configs', configs)


class AbstractStateSwitcher(ABC):

    def _update_config(self, config: Config):
        configs = ConfigManager.load()
        for i, c in enumerate(configs):
            if c.program == config.program and c.directory == config.directory and c.command == config.command:
                configs[i] = config
                break
        ConfigManager.save(configs)

    @abstractmethod
    def is_match(self) -> bool:
        pass

    @abstractmethod
    async def _switch(self):
        pass

    async def switch(self, config: Config):
        self.config = config
        if not self.is_match():
            return
        await self._switch()

    async def get_pids(self, config: Config) -> List[str]:
        pids = os.popen(
            f"ps -ef | grep '{config.command}' | grep -v grep | awk '{{print $2}}'"
        ).read().split()
        return pids

    async def is_running(self, config: Config):
        pids = await self.get_pids(config)
        return len(pids) > 0


class InitSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.init and self.config.next_state == _ProgramState.running

    async def _switch(self):
        await self.start_execute(self.config)

    async def start_execute(self, config: Config):
        if config.cur_restart >= config.max_restart:
            cf.error(
                f"restart [{config.command}] reached retry limit {config.max_restart}"
            )
            self.config.cur_state = _ProgramState.error
            self.config.next_state = _ProgramState.error
            self._update_config(self.config)

        else:
            cf.info(f'start config: {config}')
            cmd = f"{config.command} 1>> {config.stdout_file} 2>> {config.stderr_file}"
            cf.info(f"Start running [{config.command}]")
            is_running = await self.is_running(config)
            self.config.cur_state = _ProgramState.running
            self._update_config(self.config)

            if is_running:
                cf.info({'msg': 'already running', 'config': config})
            else:
                self.config.start_time = pd.Timestamp.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
                self._update_config(self.config)

                os.chdir(config.directory)
                proc = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE)
                stdout, stderr = await proc.communicate()

                # Failed to start
                if proc.returncode != 0:
                    cf.warning(
                        f"[{config.command}] is either terminated or failed to start, return code: {proc.returncode}"
                    )
                    config.cur_restart += 1
                    self._update_config(self.config)


class RunningSwitcher(AbstractStateSwitcher):

    def is_match(self):
        return self.config.cur_state == _ProgramState.running

    async def _switch(self):
        if self.config.next_state == _ProgramState.stopped:
            await self.stop_execute(self.config)

        if self.config.next_state == _ProgramState.running:
            is_running = await self.is_running(self.config)
            if is_running:
                return 
            self.config.cur_state = _ProgramState.init
            self.config.next_state = _ProgramState.running
            self._update_config(self.config)

    async def stop_execute(self, config: Config):
        cf.info(f"Stop running [{config.command}]")
        pids = await self.get_pids(config)
        self.config.cur_state = _ProgramState.stopped
        self.config.next_state = _ProgramState.stopped
        self._update_config(self.config)

        for pid in pids:
            os.system(f"kill -9 {pid}")


class StopSwitcher(AbstractStateSwitcher):

    def is_match(self) -> bool:
        return self.config.cur_state == _ProgramState.stopped

    async def _switch(self):
        if self.config.next_state in (_ProgramState.init,
                                      _ProgramState.running):
            self.config.cur_state = _ProgramState.init
            self.configs.next_state = _ProgramState.running
            self._update_config(self.config)


class Context(object):

    def __init__(self):
        self.switchers = [RunningSwitcher(), InitSwitcher(), StopSwitcher()]

    async def run(self):
        configs = ConfigManager.load()
        tasks = []
        for config in configs:
            for switcher in self.switchers:
                tasks.append(asyncio.create_task(switcher.switch(config)))
        # await asyncio.gather(*tasks)
        # print(len(tasks))


async def knivesd():
    """Run as a daemon."""
    cf.info('knivesd started')
    context = Context()
    while True:
        await asyncio.sleep(1)
        await context.run()


def start(config_or_proc_name: str):
    """Start a program."""
    configs = ConfigManager.load()
    if cf.io.exists(config_or_proc_name):
        config = parse_config_from_file(config_or_proc_name)
    else:
        config = next((c for c in configs if c.program == config_or_proc_name),
                      None)

    if config:
        config.cur_state = _ProgramState.init
        config.next_state = _ProgramState.running
        c = next((_ for _ in configs if _ == config), None)
        if c:
            config.start_time = c.start_time
        ConfigManager.add(config)
        cf.info(f"[{config.command}] started")
    else:
        cf.info(f"config not found: {config_or_proc_name}")


def stop(proc: str):
    """Stop a program."""
    program = ConfigManager.stop_by_program_name(proc)
    cf.info(f"[{program}] stopped")


def restart(proc: str):
    """Restart a program."""
    stop(proc)
    start(proc)


def status(proc: str = None):
    """Show status of a program."""
    configs = ConfigManager.load()
    if proc:
        configs = [c for c in configs if c.program == proc]

    for config in configs:
        uptime = pd.Timestamp.now() - pd.Timestamp(config.start_time)
        seconds = uptime.total_seconds()
        uptime_str = cf.fp.readable_time(seconds)
        msg = "{:<15} | {:<10} | {:<30} | {:<20}".format(
            ' -> '.join([config.cur_state, config.next_state]), config.program,
            config.command, uptime_str)
        print(msg)


if __name__ == '__main__':
    fire.Fire()

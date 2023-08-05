#!/usr/bin/env python3
import sys
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

from .urlmanager import UrlManagerFactory
from .roundcorner import RoundCornerFactory
from .fund import FundFactory

class CommandFactoryRegistry(object):

    _registry = {}
    _help_message = {}

    @classmethod
    def register_factory(cls, name: str, factory):
        cls._registry[name] = factory
        cls._help_message[name] = factory.inspect_command()

    @classmethod
    def display_help_message(cls):
        for key, value in cls._help_message.items():
            print(key, value)

    @classmethod
    def create_command(cls, name: str, *args):
        if name not in cls._registry:
            cls.display_help_message()
            return
        else:
            return cls._registry[name].create_command(*args)


def main():
    CommandFactoryRegistry.register_factory('-url', UrlManagerFactory())
    CommandFactoryRegistry.register_factory('-rc', RoundCornerFactory())
    CommandFactoryRegistry.register_factory('-fund', FundFactory())

    if len(sys.argv) < 2:
        CommandFactoryRegistry.display_help_message()
        return
    cmd_name = sys.argv[1]
    cmd = CommandFactoryRegistry.create_command(cmd_name, *sys.argv[2:])
    if cmd is not None:
        cmd.execute()




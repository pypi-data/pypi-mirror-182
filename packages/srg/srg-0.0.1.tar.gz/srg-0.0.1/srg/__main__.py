from __future__ import annotations
import sys
import argparse
from . import util, __version__, __package__
from ._menu import _main, _package_


def _usage() -> str:
    return util.stringbuilder(__package__, "[-h]", "[--version]",
                              util.stringbuilder("{", util.stringbuilder(*_package_, separator=','), "}"),
                              separator=" ")


def get_argument() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=__package__, usage=_usage())
    parser.add_argument('-v', '--version', action='version', help='show version number and exit', version=__version__)
    group = parser.add_argument_group("positional arguments")
    group.add_argument("command", choices=_package_)
    parser.add_argument("args", help=argparse.SUPPRESS, nargs=argparse.REMAINDER)
    parser.add_argument_group(group)
    options = parser.parse_args()
    return options


def main():
    _main()
    options = get_argument()
    util.executesyscmd(util.stringbuilder(options.command, *options.args, separator=' '))


if __name__ == "__main__":
    sys.exit(main())

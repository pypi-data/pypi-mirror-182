import sys
import art

from . import util, __package__

_package_ = ["zenpass", "sipher", "ioutil", "browseon", "savescreen", "local"]
_argv = sys.argv[1:]


def _greet():
    _greet_text = __package__
    for dep in _package_:
        if dep in _argv:
            _greet_text = util.stringbuilder(_greet_text, '-', dep, separator=' ')
            break
    art.tprint(_greet_text)


def _menu():
    _greet()


def _main():
    if '--menu' not in _argv:
        return
    sys.exit(_menu())


if __name__ == '__main__':
    sys.exit(_menu())

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import textwrap

import constants as C

from functools import partial


COLOR_CODES = {
    'normal':    u'0',
    'red':       u'0;31', 'bright red':     u'1;31',
    'green':     u'0;32', 'bright green':   u'1;32',
    'yellow':    u'0;33', 'bright yellow':  u'1;33',
    'blue':      u'0;34', 'bright blue':    u'1;34',
    'magenta':   u'0;35', 'bright magenta': u'1;35',
    'cyan':      u'0;36', 'bright cyan':    u'1;36',
    'dark gray': u'1;30', 'bright gray':    u'0;37',
    'black':     u'0;30', 'white':          u'1;37',
}


def string_color(text, color):
    """Return string with color applied"""
    return u"\033[{}m{}\033[0m".format(COLOR_CODES[color], text)


class Display(object):

    def __init__(self):
        pass

    def _wrap(self, msg):
        return '\n'.join(textwrap.wrap(msg, width=79, tabsize=C.TABSIZE,
                                       subsequent_indent=u' '* C.TABSIZE,
                                       drop_whitespace=False,
                                       replace_whitespace=False))

    def display(self, msg, color=None):
        sys.stdout.write(string_color(msg, color))

    def debug(self, msg, preformatted=False):
        if preformatted:
            new_msg = u'[DEBUG]:\n{}\n'.format(msg)
        else:
            new_msg = self._wrap(u'[DEBUG]: {}\n'.format(msg))
        self.display(new_msg, color=C.COLOR_DEBUG)

    def info(self, msg, preformatted=False):
        if preformatted:
            new_msg = u'{}\n'.format(msg)
        else:
            new_msg = self._wrap(u'{}\n'.format(msg))
        self.display(new_msg, color=C.COLOR_INFO)

    def warning(self, msg, preformatted=False):
        if preformatted:
            new_msg = u'[WARNING]:\n{}\n'.format(msg)
        else:
            new_msg = self._wrap(u'[WARNING]: {}\n'.format(msg))
        self.display(new_msg, color=C.COLOR_WARN)

    def error(self, msg, preformatted=False):
        if preformatted:
            new_msg = u'[ERROR]:\n{}\n'.format(msg)
        else:
            new_msg = self._wrap(u'[ERROR]: {}\n'.format(msg))
        self.display(new_msg, color=C.COLOR_ERROR)


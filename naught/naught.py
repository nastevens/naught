# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import textwrap
import time

import constants as C

from display import Display



class Package(object):

    def __init__(self):
        pass

    def install(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass


class PipPackage(Package):

    def __init__(self):
        self.name = None
        self.path = None


def main():
    display = Display()
    display.debug(u'This is debug output ' * 20)
    display.info(u'This is info output ' * 20)
    display.warning(u'This is warning output ' * 20)
    display.error(u'This is error output ' * 20)
    return 0


if __name__ == '__main__':
    sys.exit(main())

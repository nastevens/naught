# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Manage user directory tools.

Usage:
    naught [options] source
    naught [options] sync
    naught -h | --help
    naught --version

Options:
    -h --help          Show this help.
    --config-dir=DIR   Configuration path [default: ~/.naught/]
    --install-dir=DIR  Installation path [default: ~/.naught/installed]
"""

import click
import shutil
import sys
import textwrap
import time

import constants as C

from display import Display

@click.group()
@click.version_option()
def cli():
    """Naught tool."""


@cli.command()
def source():
    """Return shell code to source to add paths."""


@cli.command()
def sync():
    """Bring installed system into alignment with configuration"""


def make_config_dir():
    try:
        os.mkdir(os.path.expanduser(C.CONFIG_DIR))
    except FileExistsError:
        pass


def read_config_file():
    return yaml.load(os.path.join(
        os.path.expanduser(C.CONFIG_DIR), C.CONFIG_FILE))


class Package(object):

    def __init__(self):
        pass

    def source(self):
        pass

    def sync(self):
        pass


GIBO_CONFIG = {
    'name': 'gibo'
    'url': 'https://github.com/simonwhitaker/gibo',
    'binaries': ['gibo'],
    'post_cmd': '{repo_dir}/gibo --upgrade'
}

BIN_DIR = os.path.join(INSTALL_DIR, 'bin')

class GitPackage(Package):

    def __init__(self, config):
        self.config = config

    def source(self, state):
        state.paths.add(BIN_DIR)

    def _get_package_dir(self):
        # Create the package directory if it doesn't exist
        package_dir = os.path.join(C.INSTALL_DIR, self.config.name)
        os.makedirs(package_dir, exist_ok=True)
        return package_dir

    def _get_repo(self):
        repo_dir = os.path.join(self._get_package_dir(), 'git')
        try:
            repo = Repo(repo_dir)
        except: # repo doesn't exist - delete git dir and re-clone
            shutil.rmtree(repo_dir)
            repo = Repo.clone(self.config['url'], repo_dir)

    def _create_symlinks(self):
        repo_dir = os.path.join(self._get_package_dir(), 'git')
        for bin in self.config['binaries']:
            path = os.path.join(repo_dir, bin)
            symlink = os.path.join(BIN_DIR, os.path.basename(bin))
            try:
                os.symlink(path, symlink)
            except FileExistsError:
                pass

    def sync(self):
        package_dir = self._get_package_dir()
        repo = self._get_repo()
        repo.fetch()
        repo.head.reference = repo.commit('origin/master')
        self._create_symlinks()
        shcmd = sh.Command('sh')
        shcmd('-c', self.config['post_cmd'])


def main():
    display = Display()
    display.debug(u'This is debug output ' * 20)
    display.info(u'This is info output ' * 20)
    display.warning(u'This is warning output ' * 20)
    display.error(u'This is error output ' * 20)
    return 0


if __name__ == '__main__':
    sys.exit(main())

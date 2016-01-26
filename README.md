naught - A user-local tool manager
==================================

\*nix systems have long had the idea of installing tools locally to a
particular user, usually by installing into a directory like `~/local/bin` or
`~/.local/bin`. This is great! It means that a non-priviledged user can still
have his or her tools available without having to pester a system admin to add
a program, and without having to risk installing a program with carte blanche
access.

The downside to the user-local installs, however, is that there hasn't been an
easy way to keep the installed tools up-to-date. Package managers for the
system as a whole are a solved problem, but don't deal well with tools
installed only for a certain user. `naught` aims to change that.


Where did the name "naught" come from?
--------------------------------------

Every project needs a good name, and naught is no exception. The name naught is
meant to capture the (hopeful) ease with which tools may be installed - you
"naught but ask".


License
-------

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain
one at http://mozilla.org/MPL/2.0/.

# Developer environment

## Basic schroot setup

The proposed setup is `schroot`-based, and chroots can actually live
elsewhere, depending on storage, disk space, etc.:

    sudo apt install schroot debootstrap
    mkdir ~/chroots
    sudo debootstrap unstable ~/chroots/unstable-amd64-devel http://ftp.fr.debian.org/debian

Create a config file (`/etc/schroot/chroot.d/unstable-amd64-devel`)
for that brand new chroot, adjusting actual location, usernames, etc.:

    [unstable-amd64-devel]
    type=directory
    description=Debian unstable/amd64 development
    directory=/home/kibi/chroots/unstable-amd64-devel
    groups=root,kibi
    root-groups=root,kibi
    profile=default

One can then start a session within that chroot with:

    schroot -c unstable-amd64-devel

User identity is copied at the beginning of the session (various files
from `/etc` are copied to achieve this), so if one is a member of the
`sudo` group outside the chroot, one will also be a member of the
`sudo` group inside the chroot. The `sudo` package isn't installed by
default though, so one can exit the `chroot` with `exit` and start a
new session this way:

    # Regular system:
    schroot -c unstable-amd64-devel -u root
    # Inside the chroot:
    apt install -y sudo
    exit

    # Regular system:
    schroot -c unstable-amd64-devel
    # Inside the chroot:
    sudo -l

If `sudo` permissions are given without relying on the `sudo` group,
one might have to tweak the `/etc/sudoers` file inside the chroot.


## Basic packaging tools

Bare minimum to build, plus developer toolboxes, to be installed
within the chroot:

    sudo apt install -y build-essential fakeroot devscripts dh-make-golang lintian

One might want to install the `locales` package and configure it to
enable e.g. `fr_FR.UTF-8` and/or `en_US.UTF-8` locales matching the
environment variables set outside the chroot to avoid warnings and
fallback to the standard locale (`C`):

    sudo apt install -y locales
    sudo dpkg-reconfigure locales

Then of course your favorite editor, `git`, etc.

One might want to set `DISPLAY` (unset by default) to make it possible
to launch graphic applications, like `gitk`.


## APT configuration tweaks

It might be a good idea to enable source packages as well, plus
enabling the `devel` repository provided by DEBAMAX with initial
packaging work. Proposed `/etc/apt/sources.list`:

    deb     http://ftp.fr.debian.org/debian unstable main
    deb-src http://ftp.fr.debian.org/debian unstable main

    deb     [trusted=yes] https://crowdsec.apt.debamax.com devel main
    deb-src [trusted=yes] https://crowdsec.apt.debamax.com devel main

The `[trusted=yes]` property in the last two lines means there's no
need for anyone to deal with signing the repository when updating it,
but more importantly that there's no need to fiddle with keys, trust
stores, etc. in each clean-build/development chroot. The rationale is
that trusting the transport might be sufficient. The proper GPG
signing can be put into place if that isn't considered good enough.

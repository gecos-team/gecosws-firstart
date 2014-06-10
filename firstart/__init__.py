# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# This file is part of Guadalinex
#
# This software is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this package; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

__author__ = "Antonio Hernández <ahernandez@emergya.com>"
__copyright__ = "Copyright (C) 2011, Junta de Andalucía <devmaster@guadalinex.org>"
__license__ = "GPL-2"


def chef_is_configured():
    import os
    # Don't execute this assistant if chef its not configured
    
    return os.path.exists('/etc/chef.control')


def dbusservice():

    if not chef_is_configured():
        return

    import os
    from dbus.DBusService import DBusService

    s = DBusService()
    s.start()


def main():

    if not chef_is_configured():
        return

    from gi.repository import Gtk
    from firstart_lib.FirstartEntry import FirstartEntry
    from assistant.FirstartWindow import FirstartWindow
    import os

    entry = FirstartEntry()
    if entry.get_firstart() == True:
        return

    entry.set_firstart(1)
    entry.remove_flag()


    w = FirstartWindow()
    w.show()
    Gtk.main()

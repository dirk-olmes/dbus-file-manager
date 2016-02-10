#!/usr/bin/env python2

import dbus.service
import gobject
from dbus import Interface, SessionBus
from dbus.mainloop.glib import DBusGMainLoop
from os.path import basename, dirname

class XfceFileManager(object):
    def __init__(self, connection=None):
        proxy = connection.get_object('org.xfce.FileManager', '/org/xfce/FileManager')
        self.interface = Interface(proxy, 'org.xfce.FileManager')

    def ShowFolders(self, folders):
        for folder in folders:
            self.interface.DisplayFolder(folder, '', '')

    def ShowItems(self, items):
        for item in items:
            path = dirname(item)
            filename = basename(item)
            self.interface.DisplayFolderAndSelect(path, filename, '', '')

    def ShowItemProperties(self, items):
        for item in items:
            self.interface.DisplayFileProperties(item, '', '')


class ExposedFileManager(dbus.service.Object):
    BUS_NAME = 'org.freedesktop.FileManager1'
    INTERFACE = 'org.freedesktop.FileManager1'

    def __init__(self, connection, object_path):
        bus_name = dbus.service.BusName(self.BUS_NAME, connection)
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.file_manager = XfceFileManager(connection) 

    @dbus.service.method(dbus_interface=INTERFACE, in_signature='ass', out_signature='')
    def ShowFolders(self, folders, startup_id):
        self.file_manager.ShowFolders(folders)
        return None

    @dbus.service.method(dbus_interface=INTERFACE, in_signature='ass', out_signature='')
    def ShowItems(self, items, startup_id):
        self.file_manager.ShowItems(items)
        return None

    @dbus.service.method(dbus_interface=INTERFACE, in_signature='ass', out_signature='')
    def ShowItemProperties(self, items, startup_id):
        self.file_manager.ShowItemProperties(items)
        return None


if __name__ == '__main__':
    # make sure there is a run loop
    DBusGMainLoop(set_as_default=True)

    bus = SessionBus()

    # expose the file manager object
    object_path = '/org/freedesktop/FileManager1'
    filemanager = ExposedFileManager(bus, object_path)

    # now run the loop forever
    loop = gobject.MainLoop()
    loop.run()

# File Manager dbus interface bridge to XFCE's Thunar

On my [Gentoo](http://www.gentoo.org/) machine the "Show in System Explorer" menu item did not work on Eclipse. I kept getting this error message:

    Execution of 'dbus-send --print-reply --dest=org.freedesktop.FileManager1 
    /org/freedesktop/FileManager1 org.freedesktop.FileManager1.ShowItems 
    array:string:"file:/tmp/HelloWorld.java" string:""' failed with return code: 1

The `expose-filemanager.py` script exposes a dbus object that implements the [freedesktop File Manager DBus specification](http://www.freedesktop.org/wiki/Specifications/file-manager-interface/). This makes the Eclipse "Show in System Explorer" menu item work.

Just start the script in the background.

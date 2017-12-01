from gnunet import _Key, GNUNetDaemonError
import gnunet.strings as strings
import dbus
import threading
import datetime
from gi.repository import Gtk

from dbus.mainloop.glib import DBusGMainLoop, threads_init
threads_init()
DBusGMainLoop(set_as_default=True)
sysbus = dbus.SystemBus()


class MainLoop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        Gtk.main()

MainLoop()


def pythonize(arg, argtype):
    if argtype is datetime.datetime:
        if isinstance(arg, str):
            return strings.string_to_absolute_time(arg)
        if isinstance(arg. dbus.UInt64):
            return datetime.datetime(1970, 1, 1) + datetime.timedelta(microseconds=arg)
        return datetime.datetime(arg)


def dbusize(arg, pretty):
    if isinstance(arg, _Key):
        if pretty:
            return dbus.String(arg, variant_level=1)
        else:
            return dbus.Array(arg._data[:], variant_level=1, signature="y")

        # if type(arg) is gnsrecord.Data:
        # return dbus.Struct([arg._recordtype,

    if isinstance(arg, datetime.datetime):
        if pretty:
            return dbus.String(strings.absolute_time_to_string(arg), variant_level=1)
        else:
            return dbus.UInt64((arg - datetime.datetime(1970, 1, 1)).total_seconds() * 1000000, variant_level=1)


def handle_exception(e, daemon, daemon_address):
    name = e.get_dbus_name()
    message = e.get_dbus_message()
    if not name.startswith("org.freedesktop.DBus.Error."):
        raise e
    name = name[len("org.freedesktop.DBus.Error."):]

    if name == "Failed" or name == "InvalidArgs":
        raise GNUNetDaemonError(message)
    if name == "NoMemory":
        raise MemoryError(message)
    if name == "ServiceUnknown" or name == "NameHasNoOwner":
        raise GNUNetDaemonError("Failed to contact " + daemon + " daemon at " + daemon_address)
    if name == "NoReply" or name == "Timeout":
        raise GNUNetDaemonError("Did not receive reply from " + daemon + " daemon at " + daemon_address + ". Daemon might of crashed")
    raise e

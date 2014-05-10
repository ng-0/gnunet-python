import dbus

from gnunet._dbus_utils import *

from gnunet import *
import gnunet.crypto as crypto
import gnunet.gnsrecord as gnsrecord

def lookup(name, zone, record_type, only_cached):
  name = str(name)
  zone = dbusize(crypto.EcdsaPublicKey(zone), True)
  if record_type not in gnsrecord.types:
    raise ValueError("'record_type' must be one of %s" % gnsrecord.types)
  #record_type = dbus.UInt32(gnsrecord.types[record_type], variant_level=1)
  record_type = dbus.String(record_type, variant_level=1)
  only_cached = dbus.Boolean(only_cached)

  try:
    results = sysbus.get_object("gnu.gnunet.gns", "/").lookup(name, zone, record_type, only_cached)
  except dbus.DBusException as e:
    handle_exception(e, "gns", "gnu.gnunet.gns")

  ret = []
  for r in results:
    record_type = str(r[0])
    private = False
    pending = False
    shadow = False
    relative = False
    for f in r[1]:
      if f == "private":
        private = True
      if f == "pending":
        pending = True
      if f == "shadow":
        shadow = True
      if f == "relative_expiration":
        relative = True
    data = str(r[2])
    expiration_time = None
    if relative:
      expiration_time = pythonize(r[3], datetime.timedelta)
    else:
      expiration_time = pythonize(r[3], datetime.datetime)
    ret.append(gnsrecord.Data(record_type, data, expiration_time, private, pending, shadow))

  return ret


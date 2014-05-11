import dbus

import datetime

from gnunet import *
from gnunet._dbus_utils import *

import gnunet.block as block

get_requests = {}
requests_lock = threading.Lock()

class GetResult(threading.Thread):
  def __init__(self, expiry, key, get_path, put_path, block_type, data, path):
    threading.Thread.__init__(self)
    self.expiry = expiry
    self.key = key
    self.get_path = get_path
    self.put_path = put_path
    self.block_type = block_type
    self.data = data
    self.path = path
    self.daemon = True
    self.start()

  def run(self):
    request = None
    with requests_lock:
      request = get_requests[self.path]

    if request:
      if request.record_route:
        request.callback(self.block_type, self.key, self.data, self.expiry, get_path=self.get_path, put_path=self.put_path)
      else:
        request.callback(self.block_type, self.key, self.data, self.expiry)

def _result(expiry, key, get_path, put_path, block_type, data, path):
  expiry = pythonize(expiry, datetime.datetime)
  key = HashCode(key)
  get_path = list(get_path)
  put_path = list(put_path)
  block_type = str(block_type)
  data = bytearray(data)
  GetResult(expiry, key, get_path, put_path, block_type, data, path)

sysbus.add_signal_receiver(_result, "result", "gnu.gnunet.dht.get", "gnu.gnunet.dht", path_keyword="path")

class GetRequest:
  def __init__(self, path, callback, record_route):
    self._path = path
    self.callback = callback
    self.record_route = record_route

  def filter_known_results(self, keys):
    keys = dbus.Array([dbusize(HashCode(key)) for key in list(keys)], signature="v")
    try:
      sysbus.get_object("gnu.gnunet.dht", self._path).filter_known_results(keys, dbus_interface="gnu.gnunet.dht.get")
    except dbus.DBusException as e:
      handle_exception(e, "dht", "gnu.gnunet.dht")

  def stop(self):
    try:
      sysbus.get_object("gnu.gnunet.dht", self._path).stop(dbus_interface="gnu.gnunet.dht.get")
    except dbus.DBusException as e:
      handle_exception(e, "dht", "gnu.gnunet.dht")

def put(key, desired_replication_level, block_type, data, expiry=None, demultiplex_everywhere=False, record_route=False, bart=False):
  key = dbusize(HashCode(key), True)
  desired_replication_level = dbus.UInt32(desired_replication_level)
  if block_type not in block.types:
    raise ValueError("'block_type' must be one of %s" % block.types)
  block_type = dbus.String(block_type, variant_level=1)
  if expiry is not None:
    if not isinstance(expiry, datetime.datetime):
      raise TypeError("'expiry' must be a datetime.datetime")
    expiry = dbusize(expiry)
  else:
    expiry = dbus.String("end of time", variant_level=1)
  options = dbus.Array([], variant_level=1, signature="s")
  if demultiplex_everywhere:
    options += ["demultiplex_everywhere"]
  if record_route:
    options += ["record_route"]
  if bart:
    options += ["bart"]
  data = dbus.Array(bytearray(data), signature="y")

  try:
    sysbus.get_object("gnu.gnunet.dht", "/").put(key, desired_replication_level, options, block_type, data, expiry)
  except dbus.DBusException as e:
    handle_exception(e, "dht", "gnu.gnunet.dht")

def get_start(callback, block_type, key, desired_replication_level, demultiplex_everywhere=False, record_route=False, bart=False):
  if block_type not in block.types:
    raise ValueError("'block_type' must be one of %s" % block.types)
  block_type = dbus.String(block_type, variant_level=1)
  key = dbusize(HashCode(key), True)
  desired_replication_level = dbus.UInt32(desired_replication_level)
  options = dbus.Array([], variant_level=1, signature="s")
  if demultiplex_everywhere:
    options += ["demultiplex_everywhere"]
  if record_route:
    options += ["record_route"]
  if bart:
    options += ["bart"]
  
  ret = None
  try:
    with requests_lock:
      path = sysbus.get_object("gnu.gnunet.dht", "/").get_start(block_type, key, desired_replication_level, options)
      ret = GetRequest(path, callback, record_route)
      get_requests[path] = ret
  except dbus.DBusException as e:
    handle_exception(e, "dht", "gnu.gnunet.dht")

  return ret



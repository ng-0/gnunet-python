#!/usr/bin/python3

import gnunet.dht
import time

key = gnunet.HashCode("RMKN0U1JNA3PVCL148D6JI0STVG94A8A65INOK849CF1RT6BGF26AMMT14GMDMNRDFSJRJME6IKJ3LDFBUL2R1TPQJE64I55I32QN5G")

gnunet.dht.put(key, 1, "test", b"hello")

def result_callback(block_type, key, data, expiry, get_path, put_path):
  print("Got result from DHT")
  print("  block_type == %s" % repr(block_type))
  print("  key        == %s" % repr(key))
  print("  expiry     == %s" % repr(expiry))
  print("  get_path   == %s" % repr(get_path))
  print("  put_path   == %s" % repr(put_path))
  print("  data       == %s" % repr(data))

gnunet.dht.get_start(result_callback, "test", key, 1, record_route=True)

time.sleep(1)


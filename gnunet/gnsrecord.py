import datetime

dns_types = {
  "A":      1,
  "NS":     2,
  "CNAME":  5,
  "SOA":    6,
  "PTR":    12,
  "MX":     15,
  "TXT":    16,
  "AAAA":   28,
  "TLSA":   52}

gns_types = {
  "PKEY":     65536,
  "NICK":     65537,
  "LEHO":     65538,
  "VPN":      65539,
  "GNS2DNS":  65540}

types = dict(list(dns_types.items()) + list(gns_types.items()))

class Data:
  def __init__(self, record_type, data, expiration_time=None, private=None, pending=None, shadow=None):
    self.record_type = str(record_type)
    if record_type not in types:
      raise ValueError("'record_type' must be one of %s" % types)
    #self.data = bytearray(data)
    self.data = str(data)
    if expiration_time is not None and not isinstance(expiration_time, datetime.datetime) or isinstance(expiration_time, datetime.timedelta):
      raise TypeError("'expiration_time' must be a datetime.datetime or a datetime.timedelta")
    self.expiration_time = expiration_time
    self.private = private
    self.pending = pending
    self.shadow = shadow


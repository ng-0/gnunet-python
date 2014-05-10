import datetime

from gnunet import *

encTable = "0123456789ABCDEFGHIJKLMNOPQRSTUV"

def data_to_string(data):
  data = bytearray(data)
  size = len(data)
  bits = 0
  rpos = 0
  vbit = 0
  ret = ""
  while rpos < size:
    while rpos < size and vbit < 5:
      bits = (bits << 8) | data[rpos]
      rpos += 1
      vbit += 8
    while vbit >= 5:
      vbit -= 5
      ret += encTable[(bits >> vbit) & 31]
  if vbit > 0:
    ret += encTable[(bits << (5 - vbit)) & 31]
  return ret

def string_to_data(s):
  s = str(s)
  size = len(s)
  bits = 0
  rpos = 0
  vbit = 0
  ret = bytearray([])
  try:
    while rpos < size:
      while rpos < size and vbit < 8:
        bits = (bits << 5) | int(s[rpos], 32)
        rpos += 1
        vbit += 5
      while vbit >= 8:
        vbit -= 8
        ret.append((bits >> vbit) & 255)
    if vbit > 0:
      if bits & ((1 << vbit) - 1) != 0:
        raise ValueError("")
  except ValueError:
    raise ValueError("'" + s + "' is not a valid data-encoding string")
  return ret
  
def absolute_time_to_string(t):
  return t.strftime("%a %b %d %H:%M:%S %Y")

def string_to_absolute_time(s):
  if s == "end of time":
    return None
  try:
    return datetime.datetime.strptime(s, "%a %b %d %H:%M:%S %Y")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%c")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Ec")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%x")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Ex")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Y-%m-%d")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Y-%m")
  except ValueError:
    pass
  try:
    return datetime.datetime.strptime(s, "%Y")
  except ValueError:
    pass
  raise ValueError("%s is not a properly formatted time string" % s)



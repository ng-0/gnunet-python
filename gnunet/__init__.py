import gnunet.strings as strings

class GNUNetDaemonError(Exception):
  pass

class _Key:
  def __init__(self, arg, subtype, bits):
    if isinstance(arg, subtype):
      self._data = arg._data
    elif isinstance(arg, str):
      self._data = strings.string_to_data(arg)
    else:
      try:
        self._data = bytearray(arg)
      except:
        raise TypeError("'arg' must be a " + type(subtype).__name__ + ", a string or an array of bytes. Not a '" + type(arg).__name__ + "'.")

    if len(self._data) * 8 != bits:
      raise ValueError("'arg' must be a " + bits + " bit hash. Got " + len(self._data) + " bits.")

  def __str__(self):
    return strings.data_to_string(self._data)


class HashCode(_Key):
  def __init__(self, arg):
    _Key.__init__(self, arg, HashCode, 512)

  def __repr__(self):
    return "gnunet.HashCode('" + str(self) + "')"


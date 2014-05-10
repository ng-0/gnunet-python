from gnunet import _Key
import gnunet.strings as strings

class EcdsaPublicKey(_Key):
  def __init__(self, arg):
    _Key.__init__(self, arg, EcdsaPublicKey, 256)

  def __repr__(self):
    return "gnunet.crypto.EcdsaPublicKey('" + str(self) + "')"


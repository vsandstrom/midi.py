import mido

NRPN_MSB = 99
NRPN_LSB = 98
NRPN_DATA1 = 6
NRPN_DATA2 = 38
MSG = "control_change"

def cc(port, ch, addr, val):
  """
  Send a MIDI message
  """
  port.send(mido.Message(MSG, channel=ch, control=addr, value=val))


class Addr:
  """
  Contains the address component of an NRPN message
  It is up to the user to use valid numbers [0 - 127]
  """

  def __init__(self, msb, lsb):
    self.msb = msb
    self.lsb = lsb

  def __repr__(self):
    return f"{self.msb}:{self.lsb}"


class Data:
  """
  Contains the data component of an NRPN message
  It is up to the user to use valid numbers [0 - 127]
  """

  def __init__(self, coarse, fine):
    self.coarse = coarse
    self.fine = fine

  def __repr__(self):
    return f"{self.coarse} - {self.fine}"


def nrpn(port, ch: int, addr: Addr, val: Data):
  """
  Sends a string of 4 midi messages, manifesting as 
  NRPN message.
  """

  port.send(mido.Message(MSG, channel=ch, control=NRPN_MSB,   value=addr.msb))
  port.send(mido.Message(MSG, channel=ch, control=NRPN_LSB,   value=addr.lsb))
  port.send(mido.Message(MSG, channel=ch, control=NRPN_DATA1, value=val.coarse))
  port.send(mido.Message(MSG, channel=ch, control=NRPN_DATA2, value=val.fine))

"""This module implements the packet types of TFTP NAT"""

import socket
import struct
from TftpPacketTypes import *

class TftpPacketHeil(TftpPacket):
    """
::

            2 bytes
            --------
    HEIL  | 100    |
            --------
    """
    def __init__(self, name = None):
        TftpPacket.__init__(self)
        self.opcode = 100
        self.name = name

    def __str__(self):
        s = 'HEIL packet'
        return s

    def encode(self):
        """Encode the HEIL packet. This method populates self.buffer, and
        returns self for easy method chaining."""
        format = "!H%dsx" % len(name)
        self.buffer = struct.pack(format, self.opcode, self.name)
        return self

    def decode(self):
        format = "!H%dsx" % (len(self.buffer) - 3)
        self.opcode, self.name = struct.unpack(format, self.buffer)
        return self


class TftpPacketReg(TftpPacket):
    """
::

            2 bytes
            --------
    Reg  | 101    |
            --------
    """
    def __init__(self):
        TftpPacket.__init__(self)
        self.opcode = 101
        hostname = None
        port = None

    def __str__(self):
        s = 'Reg packet from: %s:%d' % (self.hostname, self.port)
        return s

    def encode(self):
        self.buffer=self.hostname + ':' + self.port
        return self;




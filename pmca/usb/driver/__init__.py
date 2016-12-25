from collections import namedtuple

from ...util import *

USB_CLASS_PTP = 6
USB_CLASS_MSC = 8

UsbDevice = namedtuple('UsbDevice', 'handle, idVendor, idProduct, type')

MSC_SENSE_OK = (0, 0, 0)

def parseMscSense(buffer):
 return parse8(buffer[2:3]) & 0xf, parse8(buffer[12:13]), parse8(buffer[13:14])

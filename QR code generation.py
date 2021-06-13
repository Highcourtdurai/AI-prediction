import pyqrcode #pip install pyqrcode
from pyqrcode import QRCode

w="www.google.com"

url=pyqrcode.create(w)

url.svg('MyQRcode.svg',scale=8)

import png #pip install pypng

url.png('Myqr.png',scale=8)
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


def qrCreate(picture_name, link):
    qr_code = pyqrcode.create(link)
    qr_code.png(picture_name, scale=5)


def qrDecode(picture_path):
    decocdeQR = decode(Image.open(picture_path))
    return decocdeQR[0].data.decode('ascii')

# Author : Samridhi Gupta
# Date   : 28/12/2024
# Project2 : QR Code with Border and Color

# pip install qrcode
# pip install pillow

import qrcode
from PIL import Image

# version - This parameter defines the size of the QR code

# ERROR_CORRECT_L: About 7% of the code can be restored.
# ERROR_CORRECT_M: About 15% of the code can be restored (default).
# ERROR_CORRECT_Q: About 25% of the code can be restored.
# ERROR_CORRECT_H: About 30% of the code can be restored.

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4)

# add_data
qr.add_data("www.linkedin.com/in/samridhi-gupta-2b50371b1")

qr.make(fit=True)

img = qr.make_image(fill_color="RED",back_color="WHITE")
img.save("SamridhiLinkedin.png")
img.show()


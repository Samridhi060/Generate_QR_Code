# Author - Samridhi Gupta
# Date - 28/12/2024
# Project - QR Code

# pip install qrcode
# pip install pillow

import qrcode as qr

# make - help to make qr code
# save - help to save qr code in forn of png file


img = qr.make("https://www.google.com")
img.save("google.png")
img.show()
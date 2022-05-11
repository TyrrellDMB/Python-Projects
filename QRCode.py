# Import QR library
import qrcode

# Data to be encoded
data = "https://tyrrelldmb.github.io/"

# Creating QR instance
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

#Adding data to the instance 'qr'
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('MyWebsiteQRCode.png')

import qrcode 

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,  # Version of the QR Code, higher number means more data and complexity
    box_size=10, # Size of each box in the QR code grid
    border=5     # Thickness of the border (minimum is 4)
)

# Data to be encoded in the QR code
data = "https://github.com/"

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="#dbb143")

# Save the QR code image to a file
img.save("QR01.png")


# install
# pip install qrcode
#pip install image
import qrcode

data = input("Enter the data you want to encode in the QR code: ")
filename = input("Enter a name for the QR image: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

if filename != '':
    output_file = filename + ".png"
else:
    output_file = "qrcode.png"
img.save(output_file)

print(f"QR code saved as {output_file}")
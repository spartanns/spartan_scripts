import qrcode

# Input data to encode
data = input("Enter text or a link to convert into a QR code: ")

# Generate QR Code
qr = qrcode.QRCode(
    version=1,  # Version 1: smallest size (21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
output_file = "qrcode.png"
img.save(output_file)

print(f"QR code saved as {output_file}!")

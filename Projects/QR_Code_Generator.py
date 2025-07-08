# Type 'pip install qrcode' in the terminal to install the QR Code Library
# Type 'pip install pillow' (QR code Library depends on the Pillow Package)
import qrcode 

link = input("Enter Link: ") 

qr = qrcode.QRCode(
        version=1,
        box_size=10,    # Size of Each Box in pixels
        border=4,       # Thickness of Border (min 4)
    )

qr.add_data(link)       # Add link data to 'qr'
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")   # Generate Image

img.save("qrcode_.png")     # Save Image

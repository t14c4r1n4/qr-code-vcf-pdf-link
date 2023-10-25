import qrcode
from PIL import Image
import zipfile
import vcard

# Function that creates a QR Code
def generate_qr_code_with_link(link, output_file):
    qr = qrcode.QRCode(
        version=1,  # int from 1 to 40 that controls the size of the QR Code (the smallest is version 1 with a matrix of 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_L, # = About 7% or less errors can be corrected.
        box_size=10, # controls the pixel size of each "box" of the QR Code
        border=4, # controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs)
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

# Output file name 
output_file = "m_qr_code.png"

# URL to your zipfile on onedrive (or others)
onedrive_url = "url_to_your_zipfile" 

# QR-Code-Data (link to zipfile on onedrive)
qr_code_data = onedrive_url
output_file = "qr_code.png"

# Generate QR-Code with link to the zipfile
generate_qr_code_with_link(qr_code_data, output_file)

print(f"Successfully saved QR-Code: {output_file}")
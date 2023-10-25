import zipfile
import vcard
import pdf

# Create a zip-file with pdf- and vCard-data
def create_zip_file(pdf_file, vcard_data, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zf:
        zf.writestr("vcard.vcf", vcard_data)
        zf.write(pdf_file, "test.pdf")
        
        
zip_file = "data.zip"
create_zip_file(pdf, vcard.vcard_data, zip_file)
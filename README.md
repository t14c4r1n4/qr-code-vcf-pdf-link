# QR-Code Generator

This is an QR-Code generator that zips the files into a single file which is linked in the QR code.

It's using the **Python Imaging Library (PIL)** and the **qrcode** library.

Documentation for the qrcode 3.0 library is available at: https://pypi.org/project/qrcode/.

How is it working?

## First step: install the qrcode library

```
    pip install qrcode
```

## Second step: vCard and pdf-file

Creates a new vcard and saves it in a variable named 'vcard_data' which is given to the 'qr_code_data' variable. Also the pdf-file is saved in the 'qr_code_data' variable.

## Third step: zipfile

The zipfile is created and saved under the filename 'data.zip'.

## Fourth and last step: make zipfile accessible

Move the zipfile to your onedrive directory and share it with others (copy the given link to the 'onedrive_url' variable).

-- TODOS --

- Implement Async/ Await Functionality for better usability

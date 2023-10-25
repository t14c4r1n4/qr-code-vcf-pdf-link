# Generates a vcard (.vcf) file

vcard_data = "FN:YOURNAME\nTEL:+00123456789\nEMAIL:testmail@test.com\n"
# also possible in vcard: 
# ORG:Google;GMail Team;Spam Detection Squad
# TITLE:Your title
# PHOTO;MEDIATYPE#image/gif:path/ url to your photo
# CALURI:http://example.com/calendar/jdoe
# CATEGORIES:swimmer,biker
# LANG:fr-CA

qr_code_data = "BEGIN:VCARD\n" + vcard_data + "\nEND:VCARD"
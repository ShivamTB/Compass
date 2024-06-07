import email, smtplib, ssl
import segno

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

qrcode = segno.make_qr("I will be king of the pirates!")
qrcode.save("basic_qrcode.png", scale=5, border=0)
port = 465  # For SSL
password = "ckmrbvysgxynbvud"

# Create a secure SSL context
context = ssl.create_default_context()

subject = "Welcome to Compass!"

sender_email = "compass.strawhats@gmail.com"
receiver_email = "nakul1010@gmail.com"
message = "TEST"

message = MIMEMultipart()
msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<center><img src="https://i.imgur.com/514aUua.jpeg" height="150" width="150">'
                   '<h1>Welcome to Compass Events</h1>'
                   'Please scan the below QR code to register for the event.<br><br>'
                   '<img src="cid:image1"><br><br>'
                   'Looking forward to seeing you there.</center>', 'html')
msgAlternative.attach(msgText)

fp = open('basic_qrcode.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
# Create a multipart message and set headers

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(msgImage)

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("compass.strawhats@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message.as_string())

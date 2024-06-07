import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import segno
from django.conf import settings


def send_registeration_email(user):
    # Creating and Saving QR Code
    qr_path = os.path.join(settings.BASE_DIR, 'qr_codes')
    file_path = os.path.join(qr_path, f'{user.id}.png')
    qrcode = segno.make_qr("I will be king of the pirates!")
    qrcode.save(file_path, scale=5, border=0)
    
    # Writing the Email
    port = 465  # For SSL
    password = "ckmrbvysgxynbvud"

    # Create a secure SSL context
    context = ssl.create_default_context()

    subject = f"Welcome to Compass {user.first_name}!"

    sender_email = "compass.strawhats@gmail.com"
    receiver_email = user.email

    message = MIMEMultipart()
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<center><img src="https://i.imgur.com/514aUua.jpeg" height="150" width="150">'
                       f'<h1>Welcome to Compass Events, {user.first_name}!</h1>'
                       'Please scan the below QR code at the kiosk for entry.<br><br>'
                       '<img src="cid:image1"><br><br>'
                       'Looking forward to seeing you there.</center>', 'html')
    msgAlternative.attach(msgText)

    fp = open(file_path, 'rb')
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

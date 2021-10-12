# email app for outlook users

from email.mime import text
from email.mime.nonmultipart import MIMENonMultipart
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

email_user = input("User email: ")

# # create txt file with email password in the same directory
# with open('emailpass.txt', 'r') as f:
#     email_password = f.read()

email_password = input("Password: ")

sent_from = email_user
to_email = input("Email to: ")

msg = MIMEMultipart()
msg['From'] = input("Your name: ")
msg['To'] = to_email
msg['Subject'] = input("Email subject: ")

message = input("Txt file containing message or type in message here: ")

if message.endswith('.txt'):
    with open(message, 'r') as tf:
        message = tf.read()

msg.attach(MIMEText(message, 'plain'))

trackingpixel = """
<html>
    <img src="https://pastepixel.com/image/epXZTY9QP488TV9Yq2t6.png" alt=""/>
</html>
"""
msg.attach(MIMEText(trackingpixel, 'html'))

# attach file to email
filename = input("File to attach (if any): ")

if filename != "":
    attachment = open(filename, 'rb')
    # read attachment and attach. octet-stream is the processor
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(p)

email_text = msg.as_string()

try:
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(sent_from, to_email, email_text)
    server.close()
    print('Email sent!')
except:
    print("Error occurred. Email not sent!")
import smtplib
import mimetypes
from email.message import EmailMessage
message = EmailMessage()
sender = "your-name@gmail.com"
recipient = "example@example.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Learning to send email from medium.com'
body = """Hello
I am learning to send emails using Python!!!"""
message.set_content(body)
mime_type, _ = mimetypes.guess_type('something.pdf')
mime_type, mime_subtype = mime_type.split('/')
with open('something.pdf', 'rb') as file:
 message.add_attachment(file.read(),
 maintype=mime_type,
 subtype=mime_subtype,
 filename='something.pdf')
print(message)
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_server.login("your-name@gmail.com", 'Your password')
mail_server.send_message(message)
mail_server.quit()
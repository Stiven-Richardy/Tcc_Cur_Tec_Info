import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['De'] = sender
    msg['Para'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

class servidorEmail():
    def construiEmail(self, numeroRam, mailUser):
        try:

            if(mailUser != ""):
                subject = "Email de confirmação: não responda este email!"
                body = "Código para verificação: " + str(numeroRam)
                sender = "ragequasegaming@gmail.com"
                recipients = [sender, mailUser]
                password = 'wect xolc bqlo jkxw'

                send_email(subject, body, sender, recipients, password)

        except Exception as e:
            print(e)
import smtplib
import email.message

class send_email:

    def enviar_email(self,event,sts): 

        corpo_email = event

        msg = email.message.Message()
        msg['Subject'] = sts
        msg['From'] = '...@gmail.com'
        msg['To'] = '...@gmail.com'
        password = 'password'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')

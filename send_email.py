from email.mime.text import MIMEText
import smtplib
def send_email(email,height,avg_height,count):
    from_email='amit.test1234567890@gmail.com'
    from_password='test1234567890'
    to_email=email

    subject='Height data'
    message='Hey there,your height is<strong>%s</strong>.Average height of all is <strong>%s</strong> and that is based on %s persons'%(height,avg_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)



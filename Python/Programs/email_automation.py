# Importing required Libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Providing Account Info
from_address = 'mursal.furqan@unifiedcrest.com'
to_address = ['mursalfurqan@gmail.com', 'aisha.akhtarparvaiz@gmail.com']

#Defining Variables
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = ",".join(to_address)
msg['subject'] = input("Please Enter the subject of the mail \n")
body = input("""Please write your message: """)
regards = "\n \n \nRegards \nMursal Furqan \n (0092) 343 3500305"

#Body to MIMEText
msg.attach(MIMEText("Hello\n" + body + regards, 'plain'))

email=""
password=""
# password=input("Please type your password: ")

# if email=="mursal.furqan@unifiedcrest.com":
mail = smtplib.SMTP('smtp.office365.com',587)
#Providing accesss and path for sending emails
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
#Sending Email
mail.sendmail(from_address, to_address, text)
#Closing the Mailer
mail.quit()


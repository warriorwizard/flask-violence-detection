import smtplib
import os
import getpass
import imghdr
from email.message import EmailMessage

# subject = "Account security at risk !!!\n what the fuck"
# with open(r'D:\python_\ms_teams\message.txt','r+') as msg:
# 	body=msg.read()
	
# msg = f'Subject: {subject}\n\n'	
#print(msg)
print('-'*60)
print("coded by amit".center(60, "*"))	
print('-'*60)

# passwrd=getpass.getpass(prompt='Password : ', stream=None)

# with open(r'D:\python_\ms_teams\csml.txt','r+') as rf:
# 	a=rf.readline().split(',')
# #print(a)

# for i in range(len(a)):
# 	erp=a[i].strip().strip('"').strip("'")
# 	#print(erp)
#------------------------------------------------

Sender_Email = "0201csml114@niet.co.in"
Reciever_Email = "amitech90@outlook.com"
# Reciever_Email = "0201csai107@niet.co.in"
# Password = input('Enter your email account password: ')
Password = 'india@2233'
newMessage = EmailMessage()                         
newMessage['Subject'] = "violence detected" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content(' Image attached!') 

with open('./hello.jpg', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name

newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)


#-----------------------------------------------	
# erp='0201csai107@niet.co.in'
erp='amitech90@outlook.com'
# erp='prateekasme@outlook.com'
smtp=smtplib.SMTP('smtp.office365.com',587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
# smtp.login('0201csml114@niet.co.in',passwrd)
smtp.login('0201csml114@niet.co.in','india@2233')
smtp.send_message(newMessage)
# smtp.sendmail('0201csml114@niet.co.in',erp,newMessage)
print(f'{erp} : mail_sent')
smtp.quit()

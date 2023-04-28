import smtplib
import imghdr
from email.message import EmailMessage

# Sender_Email = "0201csml114@niet.co.in"
# Reciever_Email = "amitech90@gmail.com"
# # Reciever_Email = "0201csai107@niet.co.in"
# Password = input('Enter your email account password: ')

# newMessage = EmailMessage()                         
# newMessage['Subject'] = "Check out the new logo" 
# newMessage['From'] = Sender_Email                   
# newMessage['To'] = Reciever_Email                   
# newMessage.set_content('Let me know what you think. Image attached!') 

# with open('./Endy_vector_satelliet.png ' , 'rb') as f:
#     image_data = f.read()
#     image_type = imghdr.what(f.name)
#     image_name = f.name

# newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
#     smtp.login(Sender_Email, Password)              
#     smtp.send_message(newMessage)


def mailto(img):

    Sender_Email = "0201csml114@niet.co.in"
    # Reciever_Email = "amitech90@outlook.com"
    Reciever_Email = "0201csai107@niet.co.in"
    # Reciever_Email = "0201csai107@niet.co.in"
    # Password = input('Enter your email account password: ')
    Password = input()
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "violence detected" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content(' Image attached!') 

    with open(img, 'rb') as f:
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
    smtp.login('0201csml114@niet.co.in',Password)
    smtp.send_message(newMessage)
    # smtp.sendmail('0201csml114@niet.co.in',erp,newMessage)
    print(f'{erp} : mail_sent')
    smtp.quit()

# mailto('./hello.jpg')

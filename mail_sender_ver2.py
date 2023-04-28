import smtplib
import os

smtp=smtplib.SMTP_SSL('smtp.gmail.com',2525)
smtp.ehlo()
#smtp.starttls()
smtp.ehlo()

smtp.login('Iamteamblue@proton.me','Iamcool@1')
#smtp.login('helpdeskadhi@gmail.com','pnfnvboatmczopkn')
subject = "hello"
body = "Nice to meet you!"

msg = f'Subject: {subject}\n\n{body}'

smtp.sendmail('nbody1384@gmail.com','amitech90@gmail.com',msg)


# import smtplib

# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()

# # Authentication
# s.login("sender_email_id", "sender_email_id_password")

# # message to be sent
# message = "Message_you_need_to_send"

# # sending the mail
# s.sendmail("sender_email_id", "receiver_email_id", message)

# # terminating the session
# s.quit()

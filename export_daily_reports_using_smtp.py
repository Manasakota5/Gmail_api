import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Your report is ready'
msg['From'] = 'manasasample29@gmail.com'
msg['To'] = 'manasakota.dw@gmail.com'


path = r"C:\Users\manas\Documents\Task\Junior DE Task\Junior DE Task\daily reports\2022-09-16-23-04-01-EDT-Historical-Report-ENTRFacebook-2022-06-17--2022-09-17.csv"

with open('body_part.txt') as my_file:
    data = my_file.read()
    msg.set_content(data)

with open(path,"rb") as f:
    file_data = f.read()
    print("file data in binary",file_data)
    file_name = f.name
    print("file name is ",file_name)
    msg.add_attachment(file_data,maintype="attachments",subtype="octet-stream",filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login("manasasample29@gmail.com","password")
    server.send_message(msg)


print("Email sent!!!")

# importing os and pickle module in program  
import os
import pickle
# Creating utils for Gmail APIs  
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# Importing libraries for encoding/decoding messages in base64  
from base64 import urlsafe_b64decode, urlsafe_b64encode
# Importing libraries for dealing with the attachment of MIME types in Gmail  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type

# Request all access from Gmail APIs and project  
SCOPES = ['https://mail.google.com/']
OurEmailID = 'manasasample29@gmail.com'


file_path = r"C:\Users\manas\Documents\Task\Junior DE Task\Junior DE Task\daily reports\2022-09-23-23-04-15-EDT-Historical-Report-ENTRFacebook-2022-06-24--2022-09-24.csv"

# using a default function to authenticate Gmail APIs
def authenticate():
    creds = None
    # authorizing the Gmail APIs
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
            # if creditianls is unavailable in pc
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES)  # get the credential name
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run  
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)  # using Gmail to authenticate


# Get the Gmail API service by calling the function
service = authenticate()


# Using a default funnction to add attachments in Mail
def Send_Attachment(mail, NameofFile):
    content_type, encoding = guess_mime_type(NameofFile)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'csv':  # defining csv file type attachment
        fp = open(NameofFile, 'rb')  # opening file
        msg = MIMEText(fp.read().decode(), _subtype=sub_type,filename = NameofFile)
        fp.close()
    elif main_type == 'image':  # defining image file type attachment
        fp = open(NameofFile, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type,filename = NameofFile)
        fp.close()
    elif main_type == 'audio':  # defining audio file type attachment
        fp = open(NameofFile, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type,filename = NameofFile)  # reading file
        fp.close()
    else:
        fp = open(NameofFile, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()  # closing file
    NameofFile = os.path.basename(NameofFile)
    msg.add_header('Content-Disposition', 'attachment', NameofFile=NameofFile,filename = NameofFile)
    mail.attach(msg)  # composing the mail with given attachment


# Creating mail with a default function
def creating_mail(RecieverMail, SubofMail, BodyofMail,attachments=[]):  # various import content of mail as function's parameter
    # Using if else to check if there is any attachment in mail or not  
    if not attachments:  # no attachment is given in the mail
        mail = MIMEText(BodyofMail)
        mail['to'] = RecieverMail
        mail['from'] = OurEmailID
        mail['subject'] = SubofMail
    else:  # attachment is given in the mail
        mail = MIMEMultipart()
        mail['to'] = RecieverMail
        mail['from'] = OurEmailID
        mail['subject'] = SubofMail
        mail.attach(MIMEText(BodyofMail))
        for NameofFile in attachments:
            Send_Attachment(mail, NameofFile)
    return {'raw': urlsafe_b64encode(mail.as_bytes()).decode()}


# function to send a mail
def sending_mail(service, RecieverMail, SubofMail, BodyofMail, attachments=[]):
    return service.users().messages().send(
        userId="me",
        body=creating_mail(RecieverMail, SubofMail, BodyofMail, attachments)
    ).execute()  # Body of the mail with execute() function

sending_mail(service, "manasakota.dw@gmail.com", "Your report is ready",
         "Hey manasa,find out the latest reports", [file_path])  # calling out default sending_mail() function

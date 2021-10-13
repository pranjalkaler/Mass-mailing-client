import pandas as pd
from constants import Constants as CN
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import re

class Utils:

    @staticmethod
    def read_emails():
        path = CN.FILE_DIR_PATH
        type_of_file = CN.TYPE_OF_FILE
        files = []
        e = pd.read_excel(CN.EMAIL_LIST_FILE)
        emails = e['Emails'].values
        
        return emails

    @staticmethod
    def read_pdf(file_path):
        pdfname = (file_path.split("\\"))[-1]
        print("PDF NAME: >{}<".format(pdfname))
    
        # open the file in bynary
        binary_pdf = open(file_path, 'rb')
        
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        
        # enconding the binary into base64
        encoders.encode_base64(payload)
        
        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        return payload

    @staticmethod
    def filter_emails(emails):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        valid_emails = list()
        invalid_emails = list()
        count = 0
        for email in emails:
            if isinstance(email, str):
                email = email.strip()
                if re.fullmatch(regex, email):
                    valid_emails.append(email)
                else:
                    email = "".join(email.split())
                    if "(at)" in email:
                        email = email.replace("(at)", "@")
                    if "[at]" in email:
                        email = email.replace("[at]", "@")
                    if "(AT)" in email:
                        email = email.replace("(AT)", "@")
                    if "[AT]" in email:
                        email = email.replace("[AT]", "@")
                    if "(dot)" in email:
                        email = email.replace("(dot)", ".")
                    if "[dot]" in email:
                        email = email.replace("[dot]", ".")
                    if re.fullmatch(regex, email):
                        count = count + 1
                        valid_emails.append(email)
                    else:
                        invalid_emails.append(email)
            else:
                invalid_emails.append(email)
        print("VALID EMAILS:")
        for i, e in enumerate(valid_emails):
            print(i+1, " - ", e)
        print("*" * 50)
        print("INVALID EMAILS:")
        for i, e in enumerate(invalid_emails):
            print(i+1, " - ", e)
        print("{} emails cleaned".format(count))
        
        return valid_emails, invalid_emails
    
    @staticmethod
    def create_message(toaddr):
        fromaddr = CN.EMAIL
        Message = MIMEMultipart("alternative")
        Message["Subject"] = CN.SUBJECT
        Message["from"] = fromaddr
        Message["to"] = toaddr
        html_body = CN.CONTENT
        message_body = MIMEText(html_body, "html")
        Message.attach(message_body)
        return Message
        

from constants import Constants as CN
from utils import Utils as ut
import smtplib as spd


emails = ut.read_emails()
valid_emails, invalid_emails = ut.filter_emails(emails)

fromaddr = CN.EMAIL

server = spd.SMTP("smtp.gmail.com", 587)
server.starttls()
server.ehlo()
server.login(CN.EMAIL, CN.PASSWORD)
# server.set_debuglevel(2)
pdf = ut.read_pdf(CN.PATH_TO_PDF)

for email in valid_emails:
    toaddr = email
    Message = ut.create_message(toaddr)
    Message.attach(pdf)

    print("Sending email to {}".format(toaddr))
    try:
        server.sendmail(fromaddr, toaddr, Message.as_string())
    except KeyboardInterrupt:
        break
    except:
        print("Failed to send email to {}".format(email))
server.quit()

print("Emails not sent to:")
for email in invalid_emails:
    print(email)
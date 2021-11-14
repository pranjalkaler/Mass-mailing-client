from constants import Constants as CN
from utils import Utils as ut
import smtplib as spd
import time


emails = ut.read_emails()
valid_emails, invalid_emails = ut.filter_emails(emails)

fromaddr = CN.EMAIL

server = spd.SMTP("smtp.gmail.com", 587)
server.starttls()
server.ehlo()
server.login(CN.EMAIL, CN.PASSWORD)
# server.set_debuglevel(2)
cv = ut.read_pdf(CN.PATH_TO_CV)
portfolio = ut.read_pdf(CN.PATH_TO_PORTFOLIO)
counter = 1

for email in valid_emails:
    counter = counter + 1
    toaddr = email
    Message = ut.create_message(toaddr)
    Message.attach(cv)
    Message.attach(portfolio)

    print("{} Sending email to {}".format(counter, toaddr))
    try:
        time.sleep(30)
        server.sendmail(fromaddr, toaddr, Message.as_string())
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("Failed to send email to {}".format(email))
        print("Exception: {}".format(e))
        break
server.quit()

print("Emails not sent to:")
for email in invalid_emails:
    print(email)

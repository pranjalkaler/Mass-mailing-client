class Constants:

    # Path to the root folder
    # EG: 'C:\\Users\\<my_username>\\Desktop\\MassMailer'
    FILE_DIR_PATH = ""

    # Excel file where list of emails are stored. Cell A1 should contain 'Emails'
    # File should be stored in root of the project
    EMAIL_LIST_FILE = "filename.xlsx"
    TYPE_OF_FILE = ".xls"

    #Sender email
    EMAIL = "yourname@gmail.com"
    PASSWORD = "who_let_the_dogs_out?"
    PATH_TO_PDF = "some_pdf.pdf"
    SUBJECT = "Subject of the email"

    # Populate this list with your testing emails (I used my multiple emails, 
    # as some times while testing, your sender email might get blocked)
    TEST_EMAILS = []

    CONTENT = """<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
  </head>
  <body>
    <!-- HTML formatted email body -->
  </body>
</html>"""
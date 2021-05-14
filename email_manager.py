import smtplib, os, json
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def debug_email (files):
    """
    send mail attaching debug files
    """

    # Current folder
    current_dir = os.path.dirname(__file__)

    # read credentials and config options
    config_path = os.path.join(current_dir, "config.json")
    config_data = json.loads(open(config_path, "r").read())

    # List of recipents
    to_emails = config_data["emails_to"]

    # Files
    file_list = files

    # Contect to smtp server and port
    smtpObj = smtplib.SMTP ('smtp.mail.yahoo.com', 587)

    # Send hello to smtp
    smtpObj.ehlo()

    # Active encriptation
    smtpObj.starttls()

    # Login
    email_from = config_data["email_from"]
    password = config_data["email_pass"]
    smtpObj.login (email_from, password)

    # Loop for each email in list
    for email in to_emails: 

        # Make an instance of mime multipart to create the message
        message = MIMEMultipart()

        # Add main part to the email
        message['From'] = email_from
        message["To"] = email
        message["Date"] = formatdate(localtime=True)
        message["Subject"] = "BITCLOUD TEST. Something is wrong"

        # Add tex5t to the email
        text = "BITCLOUD TEST. Something is wrong"

        message.attach (MIMEText(text))

        # Loop for files in list
        for file in file_list:

            # Read file and create email part 
            file_binary = open(file, "rb")
            part = MIMEApplication(file_binary.read(), name=os.path.basename(file))
            file_binary.close()

            # Add file to the message
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file))
            message.attach(part)

        # Send email
        smtpObj.sendmail(email_from, 
                            email, 
                            message.as_string())

        # Confirmation message
        print ("Something is wrong. Debug email send to: {}".format (email))

    # Close connection
    smtpObj.quit()

import smtplib, log, os
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.utils import formatdate

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)

class Email_manager (): 
    """Manage emails: connect and send mails
    """
    
    def __init__(self, email, password): 
        """Constrcutor of class
        """
        
        # Dictionary of server and post for smtp and imap protocol        
        servers_ports = {
            "gmail.com": {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "imap_server": "imap.gmail.com",
                "imap_port": 993
            }, 
            "outlook.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "hotmail.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "live.com": {
                "smtp_server": "smtp.office365.com",
                "smtp_port": 587,
                "imap_server": "outlook.office365.com",
                "imap_port": 993
            },
            "yahoo.com": {
                "smtp_server": "smtp.mail.yahoo.com",
                "smtp_port": 587,
                "imap_server": "imap.mail.yahoo.com",
                "imap_port": 993
            }, 
            "aol.com": {
                "smtp_server": "smtp.aol.com",
                "smtp_port": 465,
                "imap_server": "imap.aol.com",
                "imap_port": 993
            }
        }
        
        # Credentials
        self.email = email
        self.password = password
        
        # Get correct server and port
        email_domain = self.email[self.email.find("@")+1:]
        self.smtp_server = servers_ports[email_domain]["smtp_server"]
        self.smtp_port = servers_ports[email_domain]["smtp_port"]
        self.imap_server = servers_ports[email_domain]["imap_server"]
        self.imap_port = servers_ports[email_domain]["imap_port"]
        
        
    def __connect_smtp (self): 
        """Connect to smtp server for the email
        """
        
        message = "Connecting to smtp..."
        log.info(message, current_file)
        
        # Connect to server and port
        self.smtpObj = smtplib.SMTP (self.smtp_server, self.smtp_port)

        # Send hello to smtp
        self.smtpObj.ehlo()

        # Active encriptation
        self.smtpObj.starttls()

        # login
        self.smtpObj.login (self.email, self.password)
        
        message = "Connected to smtp"
        log.info(message, current_file)
    
    def send_email_text (self, receivers=[], subject="", body=""): 
        """Send email to specific receivers
        """
        
        self.__connect_smtp()
        
        # Create text menssage
        menssage = f"Subject: {subject}\n\n{body}"
        
        # Send emails
        for receiver in receivers: 
            self.smtpObj.sendmail(self.email, receiver, menssage)
            
            message = f"Sending email to: {receiver}, menssage: {menssage}"
            log.info(message, current_file)
            
        self.smtpObj.close()
            
        
        
    

# def debug_email (files):
#     """
#     send mail attaching debug files
#     """

#     # Current folder
#     current_dir = os.path.dirname(__file__)

#     # read credentials and config options
#     config_path = os.path.join(current_dir, "config.json")
#     config_data = json.loads(open(config_path, "r").read())

#     # List of recipents
#     to_emails = config_data["emails_to"]

#     # Files
#     file_list = files

#     # Contect to smtp server and port
#     smtpObj = smtplib.SMTP ('smtp.mail.yahoo.com', 587)

#     # Send hello to smtp
#     smtpObj.ehlo()

#     # Active encriptation
#     smtpObj.starttls()

#     # Login
#     email_from = config_data["email_from"]
#     password = config_data["email_pass"]
#     smtpObj.login (email_from, password)

#     # Loop for each email in list
#     for email in to_emails: 

#         # Make an instance of mime multipart to create the message
#         message = MIMEMultipart()

#         # Add main part to the email
#         message['From'] = email_from
#         message["To"] = email
#         message["Date"] = formatdate(localtime=True)
#         message["Subject"] = "BITCLOUD TEST. Something is wrong"

#         # Add tex5t to the email
#         text = "BITCLOUD TEST. Something is wrong"

#         message.attach (MIMEText(text))

#         # Loop for files in list
#         for file in file_list:

#             # Read file and create email part 
#             file_binary = open(file, "rb")
#             part = MIMEApplication(file_binary.read(), name=os.path.basename(file))
#             file_binary.close()

#             # Add file to the message
#             part['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file))
#             message.attach(part)

#         # Send email
#         smtpObj.sendmail(email_from, 
#                             email, 
#                             message.as_string())

#         # Confirmation message
#         print ("Something is wrong. Debug email send to: {}".format (email))

#     # Close connection
#     smtpObj.quit()

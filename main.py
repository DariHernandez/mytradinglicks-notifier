import json, os, log, time, bs4, datetime, pytz, calendar, sys
from web_scraping import Web_scraping
from email_manager import Email_manager
from telegram_api import telegram_bot_sendtext
from date_manager import verify_day_week, between_days, between_hours

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)


# Get credentials from config file
path_config = os.path.join(current_dir, "config.json")
with open (path_config, "r") as file_config: 
    
    # Get settings
    data_config    = json.loads(file_config.read())
    page_user      = data_config["page_user"]
    page_pass      = data_config["page_pass"]
    wait_time      = data_config["wait_time"]
    time_zone      = data_config["time_zone"]
    day_start      = data_config["day_start"].lower()
    day_end        = data_config["day_end"].lower()
    hour_start     = data_config["hour_start"]
    hour_end       = data_config["hour_end"]
    email          = data_config["email"]
    password       = data_config["password"]
    to_emails      = data_config["to_emails"]
    max_percentage = data_config["max_percentage"]
    min_percentage = data_config["min_percentage"]
    telegram_chats = data_config["telegram_chats"]


# Validate credentials
verify_day_week(day_start)   
verify_day_week(day_end) 

# Instance for webscraping
scraper = Web_scraping(headless=True)

# Login with credentials
log.info("Login to page...", print_text=True)
page_login = "https://www.mytradinglicks.com/membership-login/"
scraper.set_page(page_login)
scraper.send_data("#swpm_user_name", page_user)
scraper.send_data("#swpm_password", page_pass)
scraper.click('input[value="Login"]')
time.sleep(2)

# Connect to email
email_sender = Email_manager (email, password)

# Main loop for extract data
last_percentage = 0
while True: 
    
    # WAIT TIME
    time.sleep(wait_time)

    
    # VALIDATE DATES AND HOURS
    between_days (day_start, day_end, time_zone)
    between_hours (hour_start, hour_end, time_zone)
        
    # EXTRACT VALUE
    
    # Get correct frame 
    scraper.refresh_selenium(time_units=0.1)
    scraper.switch_to_frame('ipp_page___fCp2pxfSwTVScBqqDcbrFm_responsive')
    scraper.switch_to_frame('iframe')
    frame = scraper.get_elem('#main').get_attribute('innerHTML')
    
    # Get NDM percentage
    percentage_selector = '#container .grid-row.cells:nth-child(10) div:nth-child(4) .grid-text:nth-child(2) .text:only-child' 
    
    soup = bs4.BeautifulSoup(frame, "html.parser")
    percentage_elemn = soup.select(percentage_selector)
    percentage = int(str(percentage_elemn[0].getText()).replace("%", ""))  
    
    # NOTIFICATIONS
    
    # Detect all changes and send notifications
    if last_percentage != percentage: 


        # FIRST NOTIFICATION

        # Create email subject
        if last_percentage < percentage: 
            subject = f"Up {percentage - last_percentage}% - {percentage}%"
        else: 
            subject = f"Down {last_percentage - percentage}% - {percentage}%"
                        
        # Edit subject for first email of the day
        if last_percentage == 0:
            subject += " (first run of the program)" 
            
        # Create email body
        body = f"Last NDM percentage: {last_percentage}% \n"
        body += f"Current NDM percentage: {percentage}% \n"
        body += f"Difference: {percentage -last_percentage}%"           
        
        # Send email
        email_sender.send_email_text(to_emails, subject, body)


        # SECOND NOTIFICATION
        if percentage > max_percentage or percentage < min_percentage:
    
            # Create email subject and menssage text
            menssage_text = subject.replace(" (first run of the program)", "")
            
            # Send telegram notification 
            telegram_bot_sendtext(menssage_text, telegram_chats)
    
    
    # UPDATE LAST PERCENTAGE
    last_percentage = percentage

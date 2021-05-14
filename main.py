import json, os, log, time, bs4, datetime, pytz, calendar, sys
from web_scraping import Web_scraping
from email_manager import Email_manager

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
    day_start      = str(data_config["day_start"]).lower()
    day_end        = str(data_config["day_end"]).lower()
    hour_start     = data_config["hour_start"]
    hour_end       = data_config["hour_end"]
    email          = data_config["email"]
    password       = data_config["password"]
    to_emails      = data_config["to_emails"]
    max_percentage = data_config["max_percentage"]
    min_percentage = data_config["min_percentage"]
    
    
    
# Validate credentials (dates)
days = {
    "sunday"    : 0,
    "monday"    : 1, 
    "tuesday"   : 2,
    "wednesday" : 3,
    "thursday"  : 4,
    "friday"    : 5,
    "saturday"  : 6
}

message = "" 

if day_start not in days.keys():
    message = f"Incorrect day in config file: '{day_start}'"
    
if day_end not in days.keys(): 
    message = f"Incorrect day in config file: '{day_end}'"
    
if message: 
    log.error(message, current_file, print_text=True)
    sys.exit()
    

# Instance for webscraping
scraper = Web_scraping(headless=False)

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

    
    # VALIDATE DATES
    
    # Get date time for specific time zone
    tz = pytz.timezone(time_zone)
    time_now = datetime.datetime.now(tz)
    today = str(calendar.day_name[time_now.weekday()]).lower()
    
    # Convert dates to number
    day_start_num = days[day_start]
    day_end_num = days[day_end]
    today_num = days[today]
    
    
    # Validation of dates
    message = ""
    
    if today_num < day_start_num: 
        message = f"Current day '{today}' is before start day: '{day_start}'"
        
    if today_num > day_end_num: 
        message = f"Current day '{today}' is after end day: '{day_end}'"
        
    if message:
        log.info(message, current_file, print_text=True)
        sys.exit()       
        
    # Convert string hours to date time
    hours = int(hour_start.split(":")[0])
    minutes = int(hour_start.split(":")[1])
    hour_start_formated = datetime.time(hour=hours, minute=minutes, second=0) 
    
    hours = int(hour_end.split(":")[0])
    minutes = int(hour_end.split(":")[1])
    hour_end_formated = datetime.time(hour=hours, minute=minutes, second=0) 
    
    hour_now =  datetime.time(hour=time_now.hour, minute=time_now.minute, second=time_now.second) 
    
    print (hour_start_formated, hour_end_formated, hour_now)
    
    # Validation of hours
    message = ""
    if hour_now < hour_start_formated: 
        message = f"Current time '{hour_now}' is before start time: '{hour_start_formated}'"
        
    if hour_now > hour_end_formated: 
        message = f"Current time '{hour_now}' is after end time: '{hour_end_formated}'"
        
    if message:
        log.info(message, current_file, print_text=True)
        sys.exit()  
   
   
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
                        
        # Edit fubject for first email of the day
        if last_percentage == 0:
            subject += " (first run of the program)" 
            
        # Create email body
        body = f"Last NDM percentage: {last_percentage}% \n"
        body += f"Current NDM percentage: {percentage}% \n"
        body += f"Difference: {percentage -last_percentage}%"           
        
        # Send email
        email_sender.send_email_text(to_emails, subject, body)


        # # SECOND NOTIFICATION
        
        # # Create email subject and menssage text
        # menssage_text = subject
        # subject = subject.replace("-", "/")
        
        # # Send telegram
        # email_sender.send_email_text(to_emails, subject, body)

        # # Send telegram notification 
    
        
        
    # UPDATE LAST PERCENTAGE
    last_percentage = percentage

import json, os, log, time, bs4, datetime, pytz, calendar, sys
from web_scraping import Web_scraping
current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)


# Get credentials from config file
path_config = os.path.join(current_dir, "config.json")
with open (path_config, "r") as file_config: 
    
    # Get settings
    data_config = json.loads(file_config.read())
    page_user = data_config["page_user"]
    page_pass = data_config["page_pass"]
    wait_time = data_config["wait_time"]
    time_zone_name = data_config["time_zone_name"]
    day_start = str(data_config["day_start"]).lower()
    day_end = str(data_config["day_end"]).lower()
    
    
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

# Main loop for extract data
while True: 
    
    # WAIT TIME
    time.sleep(wait_time)

    
    # VALIDATE DATES
    
    # Get date time for specific time zone
    time_zone = pytz.timezone(time_zone_name)
    time_now = datetime.datetime.now(time_zone)
    today = str(calendar.day_name[time_now.weekday()]).lower()
    
    # Convert dates to number
    day_start_num = days[day_start]
    day_end_num = days[day_end]
    today_num = days[today]
    
    
    # Validation of dates: before and after
    message = ""
    
    if today_num < day_start_num: 
        message = f"Current day '{today}' before start day: '{day_start}'"
        
    if today_num > day_end_num: 
        message = f"Current day '{today}' after end day: '{day_end}'"
        
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
    
    
    
    # DETECT CHANGES
    
        # Send email notification
        
        # Send telegram notification 
    

input ('End?')

import json, os, log, time, bs4
from web_scraping import Web_scraping
current_dir = os.path.dirname(__file__)


# Read credentials
path_config = os.path.join(current_dir, "config.json")
with open (path_config, "r") as file_config: 
    data_config = json.loads(file_config.read())
    page_user = data_config["page_user"]
    page_pass = data_config["page_pass"]
    wait_time = data_config["wait_time"]

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

import sys, os, log, pytz, datetime, calendar, time

current_dir = os.path.dirname(__file__)
current_file = os.path.basename(__file__)

days = {
    "sunday"    : 0,
    "monday"    : 1, 
    "tuesday"   : 2,
    "wednesday" : 3,
    "thursday"  : 4,
    "friday"    : 5,
    "saturday"  : 6
}

def print_status (message="", type="info"):
    """Print status of the program and write log file, after end program

    Args:
        message (str, optional): Debug menssage. Defaults to "".
        type (str, optional): Type of menssage: info / error. Defaults to "info".
    """
    
    if message: 
        
        message += ". Program end"
        
        if type == "info":
            log.info(message, current_file, print_text=True)
        else: 
            log.error(message, current_file, print_text=True)
            
        sys.exit()

def verify_day_week (day_text):
    """
    Validate if string a day of the week
    
    Args:
        day_text (str): day of the week, as monday
    """
    

    message = "" 

    if day_text not in days.keys():
        message = f"Incorrect day in config file: '{day_text}'"
        
    print_status(message, type="error")

def get_time_now (time_zone=""): 
    """Get the current date time, with or without time zone

    Args:
        time_zone (str, optional): String of time zone like "Europe/Dublin". Defaults to "".

    Returns:
        datetime: datetime object of current datetime
    """
    
    if time_zone: 
        tz = pytz.timezone(time_zone)
        return datetime.datetime.now(tz)
    else: 
        return datetime.datetime.now()
    

def between_days (day_start, day_end, time_zone=""): 
    """Validate if current day is between specific range of days

    Args:
        day_start (int): Number of week day, between 0 and 6, with sunday as start or the week
        day_end (int): Number of week day, between 0 and 6, with sunday as start or the week
        time_zone (str, optional): String of time zone like "Europe/Dublin". Defaults to "".
    """
    
    # Get date time for specific time zone
    time_now = get_time_now(time_zone)
    today = str(calendar.day_name[time_now.weekday()]).lower()
    
    # Convert dates to number
    day_start_num = days[day_start]
    day_end_num = days[day_end]
    today_num = days[today]
    
    
    # Validation of dates and time wait
    while True:
        
        message = ""
        
        if today_num < day_start_num: 
            message = f"Current day '{today}' is before start day: '{day_start}'"
            print (message)
            time.sleep(1)
            
        elif today_num > day_end_num: 
            message = f"Current day '{today}' is after end day: '{day_end}'"
            print (message)
            time.sleep(1)
        else: 
            break
        

def between_hours (hour_start, hour_end, time_zone=""): 
    """Validate if current hour is between specific range of hours

    Args:
        day_start (String): Start hour with the structure: hh:mm
        day_end (int): End hour with the structure: hh:mm
        time_zone (str, optional): String of time zone like "Europe/Dublin". Defaults to "".
    """
    
    time_now = get_time_now(time_zone)
    
    # Convert string hours to date time
    hours = int(hour_start.split(":")[0])
    minutes = int(hour_start.split(":")[1])
    hour_start_formated = datetime.time(hour=hours, minute=minutes, second=0) 
    
    hours = int(hour_end.split(":")[0])
    minutes = int(hour_end.split(":")[1])
    hour_end_formated = datetime.time(hour=hours, minute=minutes, second=0) 
    
    hour_now =  datetime.time(hour=time_now.hour, minute=time_now.minute, second=time_now.second) 
        
    # Validation of dates and time wait
    while True:
        message = ""
        
        if hour_now < hour_start_formated: 
            message = f"Current time '{hour_now}' is before start time: '{hour_start_formated}'"
            print (message)
            time.sleep(1)
            
        elif hour_now > hour_end_formated: 
            message = f"Current time '{hour_now}' is after end time: '{hour_end_formated}'"
            print (message)
            time.sleep(1)
        else: 
            break
                
    
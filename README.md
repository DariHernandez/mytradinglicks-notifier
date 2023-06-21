<div><a href='https://github.com/darideveloper/mytradinglicks-notifier/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/mytradinglicks-notifier.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/mytradinglicks-notifier/blob/master/logo.png?raw=true' alt='Mytradinglicks Notifier' height='80px'/>

# Mytradinglicks Notifier

Emails and telegram notification for changes detected in page: https://www.mytradinglicks.com/heat-gauge-live/

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Install

## Modules

Install the next modules from pip, to use the project:

* pytz
* bs4
* requests
* selenium
* webdriver-manager
* fake-useragent

## Programs

Install the next programs, to use the project:

* google chrome

# Settings

The config.json file have the basic configurations of the project. Update it with your information / preferences

## config.json structure
```json
{
    "page_user": "your_user", 
    "page_pass": "your_password",
    "wait_time": 1,
    "time_zone": "Europe/Dublin",
    "day_start": "monday",
    "day_end": "friday",
    "hour_start": "14:30",
    "hour_end": "21:00",
    "email": "your_email@yahoo.com",
    "password": "your password",
    "to_emails": ["email1", "email2"],
    "max_percentage": 59,
    "min_percentage": 53,
    "telegram_chats": ["1812619688", "1207825117", "1308170953"], 
    "bot_token": "1853683882:AAH_XXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

### page_user
*(Type: String)*

**User name** for make **login** in project page.

### page_pass
*(Type: String)*

**User password** for make **login** in project page.

### wait_time
*(Type: Integer)*

**Waiting time in seconds** between each update, to **detect changes** on the page

### time_zone
*(Type: String)*

**Time zone text**, for manage **dates and times**. 

Sample: Europe/Dublin


### day_start
*(Type: String)*

**Day** of the week the **program** will **start**.

Possible values: **sunday, monday, tuesday, wednesday, thursday, friday, saturday**

Note: the **week starts on Sunday**.


### day_end
*(Type: String)*

**Day** of the week the **program** will **end**.

Possible values: **sunday, monday, tuesday, wednesday, thursday, friday, saturday**

Must be **any day after day_start**.

Note: the **week starts on Sunday**. 


### hour_start
*(Type: String)*

**Time** the program **will start**.

Format: **hh:mm**


### hour_end
*(Type: String)*

**Time** the program **will start**.

Format: **hh:mm**

It must be **any time after hour_start**.


### email
*(Type: String)*

**Email** that will **send** the **notification** emails.

Supported mail services:
* **gmail.com**
* **outlook.com**
* **hotmail.com**
* **live.com**
* **yahoo.com**
* **aol.com**

Note: **some mail services require additional steps to log in**. If you have problems connecting your email with the project, **contact me**.


### password
*(Type: String)*

**Password** from email that will **send** the **notification** emails.


### to_emails
*(Type: List of strings)*

**List of emails** that **will receive notifications**.


### max_percentage
*(Type: Integer)*

Reference percentage.
When the **value extracted** from the page is **greater than max_percentage**, the **second notification will be sent** (message by telegram)

Value **between 0 and 100**


### min_percentage
*(Type: Integer)*

Reference percentage.
When the **value extracted** from the page is **less than min_percentage**, the **second notification will be sent** (message by telegram)

Value **between 0 and 100**


### telegram_chats
*(Type: list of strings)*

List of **chat ids** (users), which **will receive notifications** in telegram.

Note: **Do not touch.**


### bot_token
*(Type: string)*

**Key** to connect to **telegram preconfigured bot**.

Note: **Do not touch.**

# Run

Run the `main.py` file with your python interpreter

```python
python main.py
```

# Roadmap

* [X] Load page and login with selenium
* [X] Submit telegram messages
* [X] Submit emails
* [X] Validate start and end times


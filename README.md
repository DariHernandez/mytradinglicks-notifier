<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
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

Start date: **2021-05-13**

Last update: **2023-03-28**

Project type: **client's project**

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

## Modules\r
\r
Install the next modules from pip, to use the project:\r
\r
* pytz\r
* bs4\r
* requests\r
* selenium\r
* webdriver-manager\r
* fake-useragent\r
\r
## Programs\r
\r
Install the next programs, to use the project:\r
\r
* google chrome

# Settings

The config.json file have the basic configurations of the project. Update it with your information / preferences\r
\r
## config.json structure\r
\\`\\`\\`json\r
{\r
    \\\"page_user\\\": \\\"your_user\\\", \r
    \\\"page_pass\\\": \\\"your_password\\\",\r
    \\\"wait_time\\\": 1,\r
    \\\"time_zone\\\": \\\"Europe/Dublin\\\",\r
    \\\"day_start\\\": \\\"monday\\\",\r
    \\\"day_end\\\": \\\"friday\\\",\r
    \\\"hour_start\\\": \\\"14:30\\\",\r
    \\\"hour_end\\\": \\\"21:00\\\",\r
    \\\"email\\\": \\\"your_email@yahoo.com\\\",\r
    \\\"password\\\": \\\"your password\\\",\r
    \\\"to_emails\\\": [\\\"email1\\\", \\\"email2\\\"],\r
    \\\"max_percentage\\\": 59,\r
    \\\"min_percentage\\\": 53,\r
    \\\"telegram_chats\\\": [\\\"1812619688\\\", \\\"1207825117\\\", \\\"1308170953\\\"], \r
    \\\"bot_token\\\": \\\"1853683882:AAH_XXXXXXXXXXXXXXXXXXXXXXXXXX\\\"\r
}\r
\\`\\`\\`\r
\r
### page_user\r
*(Type: String)*\r
\r
**User name** for make **login** in project page.\r
\r
### page_pass\r
*(Type: String)*\r
\r
**User password** for make **login** in project page.\r
\r
### wait_time\r
*(Type: Integer)*\r
\r
**Waiting time in seconds** between each update, to **detect changes** on the page\r
\r
### time_zone\r
*(Type: String)*\r
\r
**Time zone text**, for manage **dates and times**. \r
\r
Sample: Europe/Dublin\r
\r
\r
### day_start\r
*(Type: String)*\r
\r
**Day** of the week the **program** will **start**.\r
\r
Possible values: **sunday, monday, tuesday, wednesday, thursday, friday, saturday**\r
\r
Note: the **week starts on Sunday**.\r
\r
\r
### day_end\r
*(Type: String)*\r
\r
**Day** of the week the **program** will **end**.\r
\r
Possible values: **sunday, monday, tuesday, wednesday, thursday, friday, saturday**\r
\r
Must be **any day after day_start**.\r
\r
Note: the **week starts on Sunday**. \r
\r
\r
### hour_start\r
*(Type: String)*\r
\r
**Time** the program **will start**.\r
\r
Format: **hh:mm**\r
\r
\r
### hour_end\r
*(Type: String)*\r
\r
**Time** the program **will start**.\r
\r
Format: **hh:mm**\r
\r
It must be **any time after hour_start**.\r
\r
\r
### email\r
*(Type: String)*\r
\r
**Email** that will **send** the **notification** emails.\r
\r
Supported mail services:\r
* **gmail.com**\r
* **outlook.com**\r
* **hotmail.com**\r
* **live.com**\r
* **yahoo.com**\r
* **aol.com**\r
\r
Note: **some mail services require additional steps to log in**. If you have problems connecting your email with the project, **contact me**.\r
\r
\r
### password\r
*(Type: String)*\r
\r
**Password** from email that will **send** the **notification** emails.\r
\r
\r
### to_emails\r
*(Type: List of strings)*\r
\r
**List of emails** that **will receive notifications**.\r
\r
\r
### max_percentage\r
*(Type: Integer)*\r
\r
Reference percentage.\r
When the **value extracted** from the page is **greater than max_percentage**, the **second notification will be sent** (message by telegram)\r
\r
Value **between 0 and 100**\r
\r
\r
### min_percentage\r
*(Type: Integer)*\r
\r
Reference percentage.\r
When the **value extracted** from the page is **less than min_percentage**, the **second notification will be sent** (message by telegram)\r
\r
Value **between 0 and 100**\r
\r
\r
### telegram_chats\r
*(Type: list of strings)*\r
\r
List of **chat ids** (users), which **will receive notifications** in telegram.\r
\r
Note: **Do not touch.**\r
\r
\r
### bot_token\r
*(Type: string)*\r
\r
**Key** to connect to **telegram preconfigured bot**.\r
\r
Note: **Do not touch.**

# Run

Run the \\`main.py\\` file with your python interpreter\r
\r
\\`\\`\\`python\r
python main.py\r
\\`\\`\\`

# Roadmap

* [X] Load page and login with selenium\r
* [X] Submit telegram messages\r
* [X] Submit emails\r
* [X] Validate start and end times



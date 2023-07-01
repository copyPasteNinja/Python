#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time, random

## Username & password of your instagram account: 
my_username = ""
my_password = ""

# Instagram username list for DM:
usernames = ['user1', 'user2', 'user3']

# Messages:
messages = ['Hey! Pls follow my page', 'Hey, how are you doing?', 'Hey']

# Delay time between messages in sec:
between_messages = 2000
browser = webdriver.Chrome('chromedriver')

# Authorication:

def auth(username, password):
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(2, 4))

        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(username)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(password)
        time.sleep(random.randrange(1, 2))
        input_password.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()


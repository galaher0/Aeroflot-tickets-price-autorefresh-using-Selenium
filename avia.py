from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from avia_func import *
import os

profile = FirefoxProfile("/home/kodo/.mozilla/firefox/xtw6q8be.default")
browser = webdriver.Firefox(profile)
browser.implicitly_wait(20)
browser.get('https://www.aeroflot.ru/ru-ru')

browser.set_window_position(67, 27)
browser.set_window_size(842, 1013)
time.sleep(60)

browser.set_window_position(67, 474)
browser.set_window_size(802, 566)
previous_prices, _, _ = cycle(browser)

while True:
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    msg = '\n' + time_now + '\n' + "Price has changed for the following flight's:\n"
    try:
        print('\n' + time_now)
        prices, list_msg, full_string_msg = cycle(browser)
    except:
        print("Error occurred")
        time.sleep(60)
        browser.refresh()
        browser.find_element_by_css_selector('a.button').click()
        browser.find_element_by_css_selector("div.price-chart__col:nth-child(7) > div:nth-child(1)").click()
        continue
    for i in range(len(prices)):
        if prices[i] != previous_prices[i]:
            msg += list_msg[i] + '. Was: ' + previous_prices[i] + '\n'
    if prices != previous_prices:
        msg += "\nCurrent prices are the following:\n" + full_string_msg
        print(msg)
        send_email(msg)
        for i in range(2):
            os.system("/usr/bin/canberra-gtk-play --id='bell'")
        print("Sound played")
    previous_prices = prices
    time.sleep(300)
    

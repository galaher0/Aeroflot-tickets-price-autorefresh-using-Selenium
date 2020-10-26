import smtplib

def cycle(browser):
    date_29_dec = "\n29 December\n"
    browser.find_element_by_css_selector("div.price-chart__col:nth-child(3) > \
    div:nth-child(1)").click()
    only_straight_check(browser)
    msg_29_dec = extract_info(browser)
    
    date_30_dec = "\n30 December\n"
    browser.find_element_by_css_selector("div.price-chart__col:nth-child(6) > \
    div:nth-child(1)").click()
    only_straight_check(browser)
    msg_30_dec = extract_info(browser)
    
    date_31_dec = "\n31 December\n"
    browser.find_element_by_css_selector("div.price-chart__col:nth-child(6) > \
    div:nth-child(1)").click()
    only_straight_check(browser)
    msg_31_dec = extract_info(browser)
    
    prices = [msg_29_dec[0], msg_29_dec[1], 
              msg_30_dec[0], msg_30_dec[1], 
              msg_31_dec[0], msg_31_dec[1]]
    list_msg = [msg_29_dec[2], msg_29_dec[3],
                msg_30_dec[2], msg_30_dec[3],
                msg_31_dec[2], msg_31_dec[3]]
    full_string_msg = (date_29_dec + msg_29_dec[4] + date_30_dec 
                + msg_30_dec[4] + date_31_dec + msg_31_dec[4])
    return prices, list_msg, full_string_msg

def only_straight_check(browser):
    browser.find_element_by_css_selector(".h-pull--left .h-display--inline").click()

def extract_info(browser):
    while True:
        try:
            time_departure1 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(3) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1)").text
            airport_departure1 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(3) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(2)").text
            time_destination1 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(3) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > \
            div:nth-child(2) > span:nth-child(1)").text
            airport_destination1 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(3) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > \
            div:nth-child(1)").text
            price1 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(3) > \
            div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").text
            price1 = price1.split(' ')[0]

            print(time_departure1, airport_departure1, '--', airport_destination1,
                  time_destination1, ' price:', price1)
            message1 = "{} {} -- {} {} price: {}".format(
                time_departure1, airport_departure1, airport_destination1,
                time_destination1, price1)

            time_departure2 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(2) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1)").text
            airport_departure2 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(2)\
            > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(2)").text
            time_destination2 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(2)\
            > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
            div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > \
            div:nth-child(2) > span:nth-child(1)").text
            airport_destination2 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)").text
            price2 = browser.find_element_by_css_selector("div.flight-search__inner:nth-child(2) > \
            div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").text
            price2 = price2.split(' ')[0]

            print(time_departure2, airport_departure2, '--', airport_destination2,
                  time_destination2, ' price:', price2)
            message2 = "{} {} -- {} {} price: {}".format(
                time_departure2, airport_departure2, airport_destination2,
                time_destination2, price2)
            full_message = f'{message1}\n{message2}\n'
            return price1, price2, message1, message2, full_message
        except:
            time.sleep(10)
            browser.refresh()
            continue

def send_email(msg):
    
    import config
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_user = config.gmail_user
    app_pswd = config.app_pswd
    to = config.to
    
    sent_from = gmail_user 
    subject = 'Price has changed'
    try:
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_user, app_pswd)
        server.sendmail(gmail_user, to, msg)
        server.close()

        print('Email sent!')
    
    except:  
        print('Something went wrong...')

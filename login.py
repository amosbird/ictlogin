#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
import subprocess
import signal

def connect(username, password):
    logging.info("Connecting")
    driver = webdriver.PhantomJS()
    driver.get('http://159.226.39.22/srun_portal_pc.php?ac_id=1&')

    username_element = driver.find_element_by_name("username")
    username_element.send_keys(username)
    password_element = driver.find_element_by_id('password')
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

    logging.info("Connected")
    time.sleep(1)
    
    try:
        driver.service.process.send_signal(signal.SIGTERM)
        driver.quit()
    except Exception as e:
        # Maybe this is a bug of the selenium package
        # Stackoverflow says updating to the newest
        # version fix this, but we just ignore it here
        logging.exception("Catched error")

def connected():
    response = subprocess.check_output(['curl', '-s', 'www.baidu.com'])
    if '159.226.39.22' in response:
        logging.info("No internet connection")
        return False
    else:
        logging.info("Internet is on")
        return True
    
if __name__ == '__main__':
    # Setting up logging
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s][%(asctime)s %(filename)s:%(lineno)d]  %(message)s',
        datefmt='%Y %H:%M:%S',
    )

    # Reading account info
    try:
        with open("account.conf", "r") as f:
            username = f.readline().strip('\n')
            password = f.readline().strip('\n')
    except Exception as e:
        logging.error('please create `account.conf` with the first line '
                      'as your username and second line as your password')
        exit(1)

    # Infinite loop
    while True:
        if not connected():
            connect(username, password)
        time.sleep(300)
    

#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
import subprocess

def connect():
    logging.info("Connecting")
    driver = webdriver.PhantomJS()
    driver.get('http://159.226.39.22/srun_portal_pc.php?ac_id=1&')

    name = driver.find_element_by_name("username")
    name.send_keys('username')
    password = driver.find_element_by_id('password')
    password.send_keys('password')
    password.send_keys(Keys.RETURN)

    logging.info("Connected")
    time.sleep(1)
    driver.quit()

def connected():
    response = subprocess.check_output(['curl', '-s', 'www.baidu.com'])
    if '159.226.39.22' in response:
        logging.info("No internet connection")
        return False
    else:
        logging.info("Internet is on")
        return True
    
if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s][%(asctime)s %(filename)s:%(lineno)d]  %(message)s',
        datefmt='%Y %H:%M:%S',
        # filename='myapp.log',
        # filemode='w'
    )
    while True:
        if not connected():
            connect()
        time.sleep(30)
    

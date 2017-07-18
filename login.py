#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get('http://159.226.39.22/srun_portal_pc.php?ac_id=1&')

name = driver.find_element_by_name("username")
name.send_keys('<username>')
password = driver.find_element_by_id('password')
password.send_keys('<password>')
password.send_keys(Keys.RETURN)

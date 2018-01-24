#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.set_window_size(1124, 850)
driver.get('http://159.226.39.22/srun_portal_pc.php?ac_id=1&')
driver.find_element_by_css_selector('input#logout.btn').click()
driver.quit()

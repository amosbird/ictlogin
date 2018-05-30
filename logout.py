#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
import os

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.set_window_size(1124, 850)
driver.get('https://gw.ict.ac.cn/srun_portal_pc.php?ac_id=1&')
driver.find_element_by_css_selector('input#logout.btn').click()
driver.quit()

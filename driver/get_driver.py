'''
user:Tina
data:2018-09-07
封装driver
'''

import os
from selenium import webdriver
class GetDriver:

    def get_driver(self):
        driverPath = os.path.abspath(os.path.dirname(__file__))
        driver = webdriver.Chrome(executable_path="{}\chromedriver.exe".format(driverPath))
        return driver

'''
coding=utf-8
Tina 2018-08-22
登录
脚本执行频率：频繁
'''
from appModules.login_action import LoginAction
from driver.get_driver import *
from driver.get_url import url,username,password
import unittest

class Login():

    @classmethod
    def test_login(cls):
        cls.driver = GetDriver().get_driver()
        cls.driver.get(url)
        cls.driver.maximize_window()
        LoginAction.login(cls.driver,username,password)
        return cls.driver

if __name__ == '__main__':
    unittest.main()
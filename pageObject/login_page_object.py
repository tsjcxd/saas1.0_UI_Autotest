from util.object_map import *


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    # 登录菜单
    def login_name_obj(self):
        element = getElement(self.driver, 'xpath', '//*[@id="wrap"]/div[1]/div/div/ul/li[5]/a')
        return element

    # 用户名
    def username_obj(self):
        element = getElement(self.driver,'name','login_name')
        return element

    # 密码
    def password_obj(self):
        element = getElement(self.driver,'name','login_pwd')
        return element

    # 登录按钮
    def login_button_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="btn_submit do_login"]')
        return element



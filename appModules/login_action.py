'''
coding=utf-8
Tina 2018-08-20
登录
'''

from pageObject.login_page_object import LoginPage


class LoginAction:

    def __init__(self):
        print("Login...")

    @staticmethod
    def login(driver,username,password):
        login = LoginPage(driver)

        # 登录按钮，进入登录页面
        login.login_name_obj().click()

        # 用户名
        login.username_obj().send_keys(username)

        # 密码
        login.password_obj().send_keys(password)

        # 登录
        login.login_button_obj().click()


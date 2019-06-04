'''
coding=utf-8
Tina 2018-08-30
会员端团课预约
脚本执行频率：较高
'''

import time
from appModules.appointment_group_course_H5_member import AppointmentGroupCourse_H5Member
from appModules.appointment_private_course_H5_member import AppointmentPrivateCourse_H5Member
from driver.get_driver import GetDriver
import unittest




class TestMemberAppoint_H5(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        print("H5会员端预约团课和私教课程")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # 登录会员：18321829313
    def test01_Login(self):
        self.driver.get("https://www.styd.cn/cm/271ce78b")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.add_cookie({"name":"sass_gym_shop_owner", "value":"0c60c7148485da5177294d6cce29a15166023ffae9b052240090bf9390252ccaa%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22sass_gym_shop_owner%22%3Bi%3A1%3Bs%3A8%3A%22271ce78b%22%3B%7D"})
        self.driver.add_cookie({"name":"sass_gym_wap", "value":"b98fdd1c2518b239a9d458d47cfa39f8be3e0846a0ede94e36d3486465f93d92a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22sass_gym_wap%22%3Bi%3A1%3Bs%3A41%3A%22a77b76ad1d20836435fd4f74f965bc1f%2315799323%22%3B%7D"})
        # 俱乐部线上测试账号会员端的登录
        # self.driver.add_cookie({"name":"sass_gym_shop_owner", "value":"4136e533b745b93827e082d5fe2d56e3e1d5e94247ea59316d410e3fcae2e68ca%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22sass_gym_shop_owner%22%3Bi%3A1%3Bs%3A8%3A%227c1bdfb0%22%3B%7D"})
        # self.driver.add_cookie({"name":"sass_gym_wap", "value":"d6d432cdc7a41f6cd0ba750bf09da7794145c2f07274637afa51ac65979329fea%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22sass_gym_wap%22%3Bi%3A1%3Bs%3A41%3A%22b70aa9c9202b10b3bc5900a393f5bda3%2313923513%22%3B%7D"})
        time.sleep(3)
        self.driver.refresh()
        time.sleep(5)


    # 预约团课
    def test02_appoint_group_course(self):
        """预约团课"""
        AppointmentGroupCourse_H5Member.appointment_group_course(self.driver)
        time.sleep(2)

    # 预约私教
    def test03_appoint_private_course(self):
        """预约私教"""
        AppointmentPrivateCourse_H5Member.appointment_private_course(self.driver)
        time.sleep(2)
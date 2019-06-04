'''
coding=utf-8
Tina 2018-08-20
添加私教课程及私教课程的设置
脚本运行频率：较高
'''


import time
from appModules.add_private_course import AddPrivateCourse
from appModules.add_private_course_paid_setting import AddPrivateCourseCardSetting
from appModules.add_private_course_price_seting import AddPrivateCoursePriceSetting
from appModules.add_coach_worktime import AddCoachWorkTime
from util.Parameterize import parameterize
from util.opeartion_json import OperetionJson
import unittest
from testScripts.test_login import Login







class TestPrivateCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("添加私教课程/私教课程的设置")
        cls.driver = Login.test_login()
        cls.paras = parameterize()
        cls.privateCourseName = cls.paras.get_params("私教自动化测试不允许删除")
        cls.opera_json = OperetionJson()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    # 添加私教课程
    def test01_add_private_course(self):
        """添加私教课程，暂时未做验证"""


        AddPrivateCourse.add_private_course(self.driver,self.privateCourseName)
        self.opera_json.check_json_value("test01_add_private_course",self.privateCourseName)
        time.sleep(2)


    # 设置私教课程的储值卡付费
    def test02_private_course_card_pay(self):
        """私教课程储值卡付费设置，暂时未做验证"""


        course_name = self.opera_json.get_data("test01_add_private_course")
        AddPrivateCourseCardSetting.add_private_course_card_setting(self.driver,course_name)
        time.sleep(2)


    # 私教课程价格设定（用于客户购买私教合同）
    def test03_private_course_price(self):
        """私教课程合同价格设置，暂时未做验证"""
        AddPrivateCoursePriceSetting.add_private_course_price_setting(self.driver)
        time.sleep(2)


    # 私教教练工作时间设置
    def test04_coach_time(self):
        """私教教练的工作时间设置，暂时未做验证"""
        AddCoachWorkTime.add_coach_worktime(self.driver)
        time.sleep(2)





if __name__ == '__main__':
    unittest.main()
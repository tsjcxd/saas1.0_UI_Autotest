'''
coding=utf-8
Tina 2018-08-20
添加团课
执行频率：较高
'''


import time
from appModules.add_group_course import AddGroupCourse
from appModules.add_group_schedule import AddGroupSchedule
from appModules.add_group_course_paid_setting import AddGroupCourseCardSetting
from util.Parameterize import parameterize
from util.check_data import CheckData
from util.opeartion_json import OperetionJson
import unittest
from testScripts.test_login import Login




class TestGroupCourse(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("添加团课")
        cls.driver = Login.test_login()
        cls.paras = parameterize()
        cls.opera_json = OperetionJson()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




    # 添加免费团课
    def test01_add_free_group_course(self):
        """添加免费团课，暂时未做验证"""
        free_course_name = self.paras.get_params("免费团课自动化")
        AddGroupCourse.add_group_course(self.driver,free_course_name)
        self.opera_json.check_json_value("test01_add_free_group_course", free_course_name)   #存到json文件
        CheckData.check_data(self.driver,'//table[@class="table-1 edit-mode"]',free_course_name,1)
        time.sleep(2)


    # 添加付费团课
    def test02_add_pay_group_course(self):
        """添加付费团课，暂时未做验证"""
        pay_course_name = self.paras.get_params("付费团课自动化")
        AddGroupCourse.add_group_course(self.driver,pay_course_name,isRun=True)
        time.sleep(2)
        AddGroupCourseCardSetting.add_Group_course_card_setting(self.driver,pay_course_name)
        self.opera_json.check_json_value("test02_add_pay_group_course", pay_course_name)
        CheckData.check_data(self.driver,'//table[@class="table-1 edit-mode"]',pay_course_name,1)
        time.sleep(2)


    # 免费团课排期
    def test03_free_group_schedule(self):
        """免费团课排期，暂时未做验证"""
        free_course_name = self.opera_json.get_data("test01_add_free_group_course")    # 依赖用例 test01_add_free_group_course
        AddGroupSchedule.add_group_schedule(self.driver,"22:00",free_course_name)
        time.sleep(2)

    # 付费团课排期
    def test04_pay_group_schedule(self):
        """付费团课排期，暂时未做验证"""
        pay_course_name = self.opera_json.get_data("test02_add_pay_group_course")      # 依赖用例 test02_add_pay_group_course
        AddGroupSchedule.add_group_schedule(self.driver,"23:00",pay_course_name)
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()
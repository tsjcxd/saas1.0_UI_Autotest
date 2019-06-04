'''
coding=utf-8
Tina 2018-09-03
删除团课
脚本执行频率：较高
'''

import time
from appModules.delete_group_course import DeleteGroupCourse
from appModules.delete_private_course import DeletePrivateCourse
from util.opeartion_json import OperetionJson
import unittest
from testScripts.test_login import Login



class TestDeleteCourse(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        cls.opera_json = OperetionJson()
        print("删除免费/付费团课/私教课程")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




    # 删除免费的团课课程及团课课表
    def test01_delete_free_group_course(self):
        """删除免费的团课课程及团课课表,暂未验证"""
        class_name = self.opera_json.get_data("test01_add_free_group_course")
        DeleteGroupCourse.delete_group_schedule(self.driver,class_name)
        DeleteGroupCourse.delete_group_setting(self.driver,class_name)
        time.sleep(2)


    # 删除付费的团课课程及团课课表
    def test02_delete_pay_group_course(self):
        """删除付费的团课课程及团课课表,暂未验证"""
        class_name = self.opera_json.get_data("test02_add_pay_group_course")
        DeleteGroupCourse.delete_group_schedule(self.driver,class_name)
        time.sleep(2)
        DeleteGroupCourse.delete_group_setting(self.driver,class_name)
        time.sleep(3)

    # 删除私教课程预约表及私教课程
    def test03_delete_private_course(self):
        """删除私教课程预约表及私教课程,暂未验证"""
        class_name = self.opera_json.get_data("test01_add_private_course")
        DeletePrivateCourse.delete_private_coach_appoint_form(self.driver,"内部测试——勿打电话",class_name)
        DeletePrivateCourse.delete_private_coach_appoint_form(self.driver, "会员",class_name)
        DeletePrivateCourse.delete_private_course(self.driver,class_name)
        time.sleep(2)
        DeletePrivateCourse.delete_coach_time(self.driver)
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()
'''
coding=utf-8
Tina 2018-08-20
admin待预约付费团课
执行频率：较高
'''



import unittest
from testScripts.test_login import Login
from util.opeartion_json import OperetionJson
from appModules.appointment_pay_group_course_PC_admin import AppointmentGroupCourse_PCAdmin
from appModules.appointment_pay_private_course_PC_admin import AppointmentPrivateCourse_PCAdmin




class TestAdminAppointCourse_PC(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = Login.test_login()
        cls.opera_json = OperetionJson()
        print("PC端admin代预约付费团课和付费私教课程")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # admin代预约付费团课
    def test01_admin_appoint_group_course(self):
        """admin代预约付费团课，暂未做验证"""
        class_schedule = self.opera_json.get_data("test02_add_pay_group_course")
        AppointmentGroupCourse_PCAdmin.appointment_group_course(self.driver,class_schedule)

    # admin代预约付费私教课程
    def test02_admin_appoint_private_course(self):
        """admin代预约付费私教课程，暂未做验证"""
        course_name = self.opera_json.get_data("test01_add_private_course")
        private_course_name = "{} | 15分钟/节".format(course_name)
        AppointmentPrivateCourse_PCAdmin.appointment_private_course(self.driver,private_course_name)



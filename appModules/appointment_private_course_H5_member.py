'''
coding=utf-8
Tina 2018-09-3
会员端私教课程预约
'''
from pageObject.group_course_H5_member_object import GroupCourse_H5Member
from pageObject.private_course_H5_member_object import PrivateCourse_H5Member
import time
from selenium.webdriver.support.ui import Select

class AppointmentPrivateCourse_H5Member:

    def __init__(self):
        print("Appoint Private Course")

    @staticmethod
    def appointment_private_course(driver):
        AppointmentPrivateCourse =PrivateCourse_H5Member(driver)

        # 底部菜单"约课"
        AppointmentPrivateCourse.go_course_table_obj().click()
        time.sleep(2)

        # 切换至私教
        AppointmentPrivateCourse.private_course_table_obj().click()
        time.sleep(5)


        # 选择测试场馆
        AppointmentPrivateCourse.store_select_obj().click()
        AppointmentPrivateCourse.store_select1_Obj().click()
        # Select(AppointmentGroupCourse.StoreSelectObj()).select_by_value("320158331")
        time.sleep(6)

        # 课程列表预约
        AppointmentPrivateCourse.appoint_obj().click()

        time.sleep(2)

        # 私教详情页面的预约
        AppointmentPrivateCourse.appoint_detail_obj().click()
        time.sleep(2)

        # 选择预约时间
        AppointmentPrivateCourse.appointment_time_obj().click()
        time.sleep(2)

        # 选择22:30分
        AppointmentPrivateCourse.specific_time_obj().click()
        time.sleep(2)

        # 确认
        AppointmentPrivateCourse.confirm_time_obj().click()
        time.sleep(5)

        # 确认预约
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
        AppointmentPrivateCourse.confirm_appoint_obj().click()
        time.sleep(2)

        AppointmentPrivateCourse.confirm_obj()

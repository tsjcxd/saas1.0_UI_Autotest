'''
coding=utf-8
Tina 2018-08-30
会员端团课预约
'''
from pageObject.group_course_H5_member_object import GroupCourse_H5Member
import time
from _datetime import datetime

class AppointmentGroupCourse_H5Member:

    def __init__(self):
        print("add GroupCourse")

    @staticmethod
    def appointment_group_course(driver):
        AppointmentGroupCourse =GroupCourse_H5Member(driver)

        # 底部菜单"约课"
        AppointmentGroupCourse.go_course_table_obj().click()
        time.sleep(2)

        # 选择测试场馆
        AppointmentGroupCourse.store_select_obj().click()
        AppointmentGroupCourse.store_select1_obj().click()
        time.sleep(6)

        # 课程列表预约
        AppointmentGroupCourse.appoint_obj().click()

        time.sleep(2)

        # 团课详情页面的预约
        AppointmentGroupCourse.appoint_detail_obj().click()
        time.sleep(2)

        # 浏览器自带的弹窗“确认”
        AppointmentGroupCourse.confirm_obj()
        time.sleep(2)

        # 浏览器自带的弹窗预约成功之后的“确认”
        AppointmentGroupCourse.confirm_obj()

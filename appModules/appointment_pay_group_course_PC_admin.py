'''
coding=utf-8
Tina 2018-08-30
管理员端代会员预约付费的团课
'''
from pageObject.group_schedule_object import GroupSchedule
import time

class AppointmentGroupCourse_PCAdmin:

    def __init__(self):
        print("add GroupCourse")

    @staticmethod
    def appointment_group_course(driver,class_schedule):
        admin_appoint_group_course = GroupSchedule(driver)

        # 进入左侧菜单“课程”
        admin_appoint_group_course.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至团课课表table
        admin_appoint_group_course.go_group_schedule_obj().click()
        time.sleep(3)

        # 选择门店
        admin_appoint_group_course.select_store_obj().click()
        time.sleep(2)

        # 选择付费的团课
        admin_appoint_group_course.select_course_obj(class_schedule).click()

        # 点击查看
        admin_appoint_group_course.view_obj().click()

        # 点击“添加团课预约”
        admin_appoint_group_course.appoint_obj().click()

        # 定位会员输入手机号及输入手机号
        admin_appoint_group_course.member_phone_obj().click()
        time.sleep(2)
        admin_appoint_group_course.member_phone_obj().send_keys("18321829313")
        time.sleep(3)

        # 选择输入的会员
        admin_appoint_group_course.search_customer_obj().click()

        # 选择会员的储值卡
        admin_appoint_group_course.select_card_obj().click()
        time.sleep(2)

        # 点击添加团课预约页面的确定按钮
        admin_appoint_group_course.group_appoint_confirm_obj().click()
        time.sleep(2)

        # 浏览器自带的确认框
        admin_appoint_group_course.group_script_confirm_obj().click()
        time.sleep(2)







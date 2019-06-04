'''
coding=utf-8
Tina 2018-08-30
管理员端代会员预约付费的私教课程
'''

from pageObject.private_coach_appoint_form_object import PrivateCoachAppointForm
from selenium.webdriver.support.select import Select
import time
class AppointmentPrivateCourse_PCAdmin:
    def __init__(self):
        print("pc端管理员代预约付费的私教课程")

    @staticmethod
    def appointment_private_course(driver,course_name):
        admin_appoint_private_course = PrivateCoachAppointForm(driver)

        # 进入左侧的菜单栏
        admin_appoint_private_course.go_course_table_obj().click()

        # 切换至私教预约表的Table
        admin_appoint_private_course.go_private_coach_appoint_form_obj().click()

        # 点击“代预约私教课程”的按钮
        admin_appoint_private_course.appoint_button_obj().click()
        time.sleep(2)

        # 选择门店
        admin_appoint_private_course.select_store_obj().click()
        time.sleep(2)

        # 定位搜索会员的输入框和输入会员的手机号
        admin_appoint_private_course.member_phone_obj().click()
        time.sleep(2)
        admin_appoint_private_course.member_phone_obj().send_keys("18321829313")
        time.sleep(2)

        # 选择会员
        admin_appoint_private_course.search_customer_obj().click()
        time.sleep(2)

        # 选择预约的课程
        Select(admin_appoint_private_course.private_course_select_obj()).select_by_visible_text(course_name)
        time.sleep(3)

        # 选择预约的储值卡
        admin_appoint_private_course.store_card_obj().click()

        # 点击下一步
        admin_appoint_private_course.pending_appoint_next_button_obj().click()

        # 选择时间及上课的教练
        admin_appoint_private_course.coach_time_obj().click()

        # 代预约页面的确定按钮
        admin_appoint_private_course.pending_appoint_confrim_button_obj().click()


'''
coding=utf-8
Tina 2018-08-20
添加私教教练的可预约时间
'''
from pageObject.coach_worktime_object import CoachWorkTime
from selenium.webdriver.support.ui import Select
import time

class AddCoachWorkTime:

    def __init__(self):
        print("add AddCoachWorkTime")

    @staticmethod
    def add_coach_worktime(driver):
        addcoachworktime =CoachWorkTime(driver)
        driver.implicitly_wait(30)

        # 左侧菜单栏：课程
        addcoachworktime.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至私教教练工作时间设置table
        addcoachworktime.go_private_coach_setting_obj().click()
        # time.sleep(2)

        # 选择私教教练
        Select(addcoachworktime.coach_select_obj()).select_by_visible_text("测试教练不要删除")

        # 点击可预约时间按钮
        addcoachworktime.add_worktime_obj().click()
        # time.sleep(2)

        # 添加可预约时间
        addcoachworktime.time_from_obj().send_keys("22:30")
        addcoachworktime.time_to_obj().send_keys("23:30")

        # 确认
        addcoachworktime.save_button_obj().click()
        # time.sleep(2)

        # 弹框确认
        addcoachworktime.confirm_button_obj().click()
        # time.sleep(2)
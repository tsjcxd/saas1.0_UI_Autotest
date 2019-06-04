'''
coding=utf-8
Tina 2018-08-20
添加私教课程
'''
from pageObject.private_course_setting_object import PrivateCourseSetting
import time

class AddPrivateCourse:

    def __init__(self):
        print("add PrivateCourse")

    @staticmethod
    def add_private_course(driver,name):
        addprivatecourse =PrivateCourseSetting(driver)
        driver.implicitly_wait(30)

        # 左侧菜单栏：课程
        addprivatecourse.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至私教课程设置table
        addprivatecourse.go_private_course_setting_obj().click()
        # time.sleep(2)

        # 点击添加按钮
        addprivatecourse.add_private_course_obj().click()
        # time.sleep(2)

        # 添加课程名字
        addprivatecourse.add_course_name_obj().send_keys(name)

        # 添加课程时长
        addprivatecourse.add_course_time_obj().send_keys(15)

        # 选择课程支持的门店
        addprivatecourse.add_course_store_obj().click()
        # time.sleep(2)

        # 选择课程支持的教练
        addprivatecourse.add_course_coach_obj().click()
        # time.sleep(2)

        # 支持储值卡购买
        addprivatecourse.add_card_obj().click()
        # time.sleep(2)

        # 确认
        addprivatecourse.add_confirm_obj().click()
        # time.sleep(2)

        # 弹框确认
        addprivatecourse.prompt_message_obj().click()
        # time.sleep(2)
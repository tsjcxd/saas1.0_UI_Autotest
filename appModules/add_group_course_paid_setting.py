'''
coding=utf-8
Tina 2018-08-20
添加团课课程的储值卡付费设置
'''

from pageObject.group_course_setting_object import GroupCourseSetting
import time

class AddGroupCourseCardSetting:

    def __init__(self):
        print("add AddGroupCourseCardSetting")

    @staticmethod
    def add_Group_course_card_setting(driver,course_name):
        addgroupcoursecardsetting =GroupCourseSetting(driver)
        driver.implicitly_wait(30)

        # 左侧菜单栏：课程
        addgroupcoursecardsetting.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至团课课程设置的table
        addgroupcoursecardsetting.go_group_course_setting_obj().click()
        # time.sleep(2)

        # 点击付费设置按钮
        addgroupcoursecardsetting.pay_card_setting_obj(course_name).click()
        time.sleep(5)

        # 为“储值卡不要删除数据”设置扣费金额：10元
        addgroupcoursecardsetting.select_card_obj().click()
        addgroupcoursecardsetting.money_setting_obj().send_keys(10)
        time.sleep(3)

        # 确认
        addgroupcoursecardsetting.confirm_button_obj().click()
        time.sleep(2)

        # 再次确认
        addgroupcoursecardsetting.queding_obj().click()
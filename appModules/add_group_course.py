'''
coding=utf-8
Tina 2018-08-20
添加团课课程
'''
from pageObject.group_course_setting_object import GroupCourseSetting
import time

class AddGroupCourse:

    def __init__(self):
        print("add GroupCourse")

    @staticmethod
    def add_group_course(driver,name,isRun=False):
        addgroupcourse =GroupCourseSetting(driver)
        driver.implicitly_wait(30)

        # 左侧菜单"课程"
        addgroupcourse.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至团课课程设置的table
        addgroupcourse.go_group_course_setting_obj().click()
        # time.sleep(2)

        # 添加团课的按钮
        addgroupcourse.add_group_course_obj().click()
        # time.sleep(2)

        # 添加名字
        addgroupcourse.add_course_name_obj().send_keys(name)

        # 添加课程时长
        addgroupcourse.add_course_time_obj().send_keys("30")

        # 选择课程支持的门店
        addgroupcourse.add_course_store_obj().click()
        # time.sleep(2)

        # 选择课程的上课教练
        addgroupcourse.add_course_coach_obj().click()
        # time.sleep(2)

        if isRun:
            # 预约另付费：是
            addgroupcourse.pay_setting_obj().click()

        # 确认
        addgroupcourse.add_confirm_obj().click()
        # time.sleep(2)

        # 弹框确认
        addgroupcourse.queding_obj().click()
        # time.sleep(2)



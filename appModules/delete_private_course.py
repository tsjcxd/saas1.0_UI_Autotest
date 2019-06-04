'''
coding=utf-8
Tina 2018-09-03
删除私教预约记录及私教课程
'''
from pageObject.group_course_setting_object import GroupCourseSetting
from pageObject.private_course_setting_object import PrivateCourseSetting
from pageObject.private_coach_appoint_form_object import PrivateCoachAppointForm
from pageObject.coach_worktime_object import CoachWorkTime
from pageObject.group_schedule_object import GroupSchedule
import time
from selenium.webdriver.support.ui import Select

class DeletePrivateCourse:

    def __init__(self,driver):
        print("Delete PrivateCourse")

    @staticmethod
    def delete_private_coach_appoint_form(driver,appoint_people,appoint_data):
        deletePrivateCoachAppointForm = PrivateCoachAppointForm(driver)

        # 左侧菜单"课程"
        deletePrivateCoachAppointForm.go_course_table_obj().click()
        time.sleep(2)

        # 切换至私教预约表
        deletePrivateCoachAppointForm.go_private_coach_appoint_form_obj().click()
        time.sleep(1)

        # 选择要删除的私教预约数据
        deletePrivateCoachAppointForm.select_record_obj(appoint_people,appoint_data).click()
        time.sleep(1)

        # 点击取消预约
        deletePrivateCoachAppointForm.cancel_appoint_obj().click()
        time.sleep(1)

        # 确认取消
        deletePrivateCoachAppointForm.confirm_delete_obj().click()
        time.sleep(1)

        # 取消预约成功之后确定
        deletePrivateCoachAppointForm.delete_success_obj().click()
        time.sleep(1)


    @staticmethod
    def delete_private_course(driver,course_name):
        deletePrivateCourse = PrivateCourseSetting(driver)
        # 进入左侧菜单栏：“课程”
        deletePrivateCourse.go_course_table_obj().click()
        time.sleep(2)

        # 切换至私教课程设置
        deletePrivateCourse.go_private_course_setting_obj().click()
        time.sleep(2)

        # 选择私教课程
        # 选择设置的私教课程(默认的新增私教课程的第一个)
        course_first_name = deletePrivateCourse.select_firse_course_obj().text
        if course_name in course_first_name:
            time.sleep(2)
        else:
            deletePrivateCourse.select_course_obj(course_name).click()
            time.sleep(2)

        # 删除课程
        deletePrivateCourse.delete_button_obj().click()
        time.sleep(2)

        # 确认删除
        deletePrivateCourse.confirm_delete_button_obj().click()
        time.sleep(3)

        # 删除成功提示按钮：确定
        deletePrivateCourse.cancel_success_button_obj().click()


    @staticmethod
    def delete_coach_time(driver):
        deleteCoachTime = CoachWorkTime(driver)
        # 进入左侧菜单栏：“课程”
        deleteCoachTime.go_course_table_obj().click()
        time.sleep(2)

        # 切换至私教教练工作时间设置
        deleteCoachTime.go_private_coach_setting_obj().click()
        time.sleep(1)

        # 下拉款中选择教练
        Select(deleteCoachTime.select_coach_obj()).select_by_visible_text("测试教练不要删除")

        # 删除教练的时间
        deleteCoachTime.delete_time_obj().click()
        time.sleep(1)

        # 浏览器弹框确认
        deleteCoachTime.confirm_obj()

        # 删除成功确认
        deleteCoachTime.delete_success().click()
        time.sleep(1)

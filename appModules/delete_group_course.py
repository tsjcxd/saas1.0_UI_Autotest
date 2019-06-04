'''
coding=utf-8
Tina 2018-09-03
删除团课课程课表及团课课程
'''
from pageObject.group_course_setting_object import GroupCourseSetting
from pageObject.group_schedule_object import GroupSchedule
import time
from selenium.webdriver.support.ui import Select
from util.opeartion_json import OperetionJson

class DeleteGroupCourse:

    def __init__(self,driver):
        print("Delete GroupCourse")

    @staticmethod
    def delete_group_schedule(driver,class_schedule):
        deleteGroupSchedule = GroupSchedule(driver)

        # 左侧菜单"课程"
        deleteGroupSchedule.go_course_table_obj().click()
        time.sleep(2)


        # 选择门店
        deleteGroupSchedule.select_store_obj().click()
        time.sleep(2)

        # 选择课程
        deleteGroupSchedule.select_course_obj(class_schedule).click()
        time.sleep(2)

        # 点击查看
        deleteGroupSchedule.view_obj().click()
        time.sleep(2)

        # 选择会员的取消预约按钮
        deleteGroupSchedule.cancel_appointment_obj().click()
        time.sleep(2)

        # 确认取消预约
        deleteGroupSchedule.confirm_button_obj().click()
        time.sleep(2)

        # 取消预约成功
        deleteGroupSchedule.cancel_success_button_obj().click()
        time.sleep(2)

        # 返回团课列表
        deleteGroupSchedule.return_list_obj().click()
        time.sleep(2)

        # 选择门店
        deleteGroupSchedule.select_store_obj().click()
        time.sleep(2)

        # 选择课程
        deleteGroupSchedule.select_course_obj(class_schedule).click()
        time.sleep(2)

        # 选择“删除课表”的按钮
        deleteGroupSchedule.delete_button_obj().click()
        time.sleep(2)

        # 浏览器自带弹框：“确认删除课表”
        deleteGroupSchedule.confirm_obj()

        # 删除成功提示
        deleteGroupSchedule.cancel_success_button_obj().click()
        time.sleep(2)



    @staticmethod
    def delete_group_setting(driver,course_name):
        deleteGroupSetting = GroupCourseSetting(driver)
        # 切换至团课课程设置的table
        deleteGroupSetting.go_group_course_setting_obj().click()
        time.sleep(2)
        # 删除团课课程
        deleteGroupSetting.delete_course_obj(course_name).click()
        time.sleep(2)
        # 确认删除
        deleteGroupSetting.confirm_delete_button_obj().click()
        time.sleep(2)
        # 删除成功提示
        deleteGroupSetting.cancel_success_button_obj().click()
        time.sleep(2)





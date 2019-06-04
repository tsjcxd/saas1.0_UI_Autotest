'''
coding=utf-8
Tina 2018-08-20
添加私教课程的价格设置
'''
from pageObject.private_course_setting_object import PrivateCourseSetting
import time

class AddPrivateCoursePriceSetting:

    def __init__(self):
        print("add AddPrivateCoursePriceSetting")

    @staticmethod
    def add_private_course_price_setting(driver):
        addprivatecoursepricesetting =PrivateCourseSetting(driver)

        # 左侧菜单栏：课程
        addprivatecoursepricesetting.go_course_table_obj().click()
        time.sleep(2)

        # 切换至私教课程设置table
        addprivatecoursepricesetting.go_private_course_setting_obj().click()
        time.sleep(2)

        # 选择设置的私教课程（默认选择新增的第一个的私教课程）
        # addprivatecoursepricesetting.select_PrivateCourseObj().click()
        # time.sleep(2)

        # 点击添加私教课程价格设定的按钮
        addprivatecoursepricesetting.add_private_course_price_obj().click()
        time.sleep(2)

        # 添加数量区间
        addprivatecoursepricesetting.add_number_from_obj().send_keys(1)
        addprivatecoursepricesetting.add_number_to_obj().send_keys(10)

        # 添加售价
        addprivatecoursepricesetting.add_price_obj().send_keys(10)

        # 添加转让的手续费
        addprivatecoursepricesetting.add_fee_obj().send_keys(10)

        # 确认
        addprivatecoursepricesetting.save_price_button_obj().click()
        time.sleep(2)

        # 弹框确认
        addprivatecoursepricesetting.confirm_price_button_obj().click()
        time.sleep(2)
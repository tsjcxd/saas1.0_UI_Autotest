'''
coding=utf-8
Tina 2018-08-20
添加私教课程的储值卡付费设置
'''

from pageObject.private_course_setting_object import PrivateCourseSetting
import time

class AddPrivateCourseCardSetting:

    def __init__(self):
        print("add AddPrivateCourseCardSetting")

    @staticmethod
    def add_private_course_card_setting(driver,course_name):
        addprivatecoursecardsetting =PrivateCourseSetting(driver)
        driver.implicitly_wait(30)

        # 左侧菜单栏：课程
        addprivatecoursecardsetting.go_course_table_obj().click()
        # time.sleep(2)

        # 切换至私教课程设置table
        addprivatecoursecardsetting.go_private_course_setting_obj().click()
        time.sleep(2)

        # 选择设置的私教课程(默认的新增私教课程的第一个)
        course_first_name = addprivatecoursecardsetting.select_firse_course_obj().text
        if course_name in course_first_name:
            time.sleep(2)
        else:
            addprivatecoursecardsetting.select_course_obj(course_name).click()
            time.sleep(2)


        # 点击付费按钮
        addprivatecoursecardsetting.pay_obj().click()
        time.sleep(5)

        # 选择储值卡
        addprivatecoursecardsetting.select_card_obj().click()
        time.sleep(5)

        # 为“储值卡不要删除数据”设置扣费金额：10元
        addprivatecoursecardsetting.money_setting_obj().send_keys(10)

        # 确认
        addprivatecoursecardsetting.save_card_button_obj().click()
        # time.sleep(2)

        # 弹框确认
        addprivatecoursecardsetting.confirm_card_button_obj().click()
        # time.sleep(2)
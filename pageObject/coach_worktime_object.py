'''
coding=utf-8
Tina 2018-08-20
私教教练工作时间设置的页面的封装
'''
from util.object_map import *

class CoachWorkTime:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    # 左侧菜单：课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[4]/a/i')
        return element

    # 切换至私教教练工作时间设置的Table
    def go_private_coach_setting_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="私教教练工作时间设置"]')
        return element

    # 私教教练下拉框
    def coach_select_obj(self):
        element = getElement(self.driver,'name','coach_id')
        return element

    # # 私教教练搜索的输入框
    # def coach_inputValueObj(self):
    #     element = getElement(self.driver,'xpath','//input[@class="select2-search__field"]')
    #     return element

    # 点击可预约时间
    def add_worktime_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="btn-medium mg-r10 add_schedule"]')
        return element

    # 开始时间——结束时间
    def time_from_obj(self):
        element = getElement(self.driver,'name','time_from')
        return element

    def time_to_obj(self):
        element = getElement(self.driver,'name','time_to')
        return element

    # 保存
    def save_button_obj(self):
        element = getElement(self.driver,'xpath','//input[@class="btn-small save"]')
        return element

    # 确认
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[@class="lay-btn-confirm"]')
        return element


    # 选择教练的下拉框
    def select_coach_obj(self):
        element = getElement(self.driver,'name','coach_id')
        return element

    # 删除教练的工作时间
    def delete_time_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="删除"]')
        return element

    # 浏览器弹框确认
    def confirm_obj(self):
        self.driver.switch_to_alert().accept()


    # 确认删除成功
    def delete_success(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element
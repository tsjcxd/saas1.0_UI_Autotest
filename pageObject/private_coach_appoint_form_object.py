'''
coding=utf-8
Tina 2018-08-20
私教预约页面
'''
from util.object_map import *
class PrivateCoachAppointForm:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    # 左侧菜单：课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[4]/a/i')
        return element

    # 切换至私教预约表的Table
    def go_private_coach_appoint_form_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="私教预约表"]')
        return element

    # 代预约私教课程按钮
    def appoint_button_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer appoint_order hastip"]')
        return element

    # 会员的门店下拉框的选择
    def select_store_obj(self):
        element = getElement(self.driver,'xpath','//div[@id="pop_layer_wrap"]//option[text()="懒猫馆——测试数据不能删除"]')
        return element

    # 添加团课预约输入手机号
    def member_phone_obj(self):
        element = getElement(self.driver,'xpath','//input[@name="se"]')
        return element

    # 筛选会员：“测试数据不要删除(18321829313)”
    def search_customer_obj(self):
        element = getElement(self.driver, 'xpath','//ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content"]//li[text()="测试数据不要删除(18321829313)"]')
        return element

    # 选择预约的私教课程
    def private_course_select_obj(self):
        element = getElement(self.driver,'name','course_cat_id')
        return element

    # 选择预约的储值卡
    def store_card_obj(self):
        element = getElement(self.driver,'xpath','//label[contains(text(),"储值卡不要删除数据")]/preceding-sibling::input')
        return element

    # 代预约私教课程页面的下一步按钮
    def pending_appoint_next_button_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="下一步"]')
        return element

    # 选择私教教练的时间
    def coach_time_obj(self):
        element = getElement(self.driver,'xpath','//p[text()="22:45"]')
        return element

    # 代预约私教课程页面的确定按钮
    def pending_appoint_confrim_button_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element

    # 选择要删除的数据
    def select_record_obj(self,appoint_people,appoint_data):
        element = getElement(self.driver,'xpath','//table[@class="table-1 edit-mode"]//td[contains(text(),"{}")]/preceding-sibling::td[text()="{}"]/preceding-sibling::td[text()="已预约"]'.format(appoint_people,appoint_data))
        return element

    # 取消课程预约
    def cancel_appoint_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer order_cancel hastip"]')
        return element

    # 取消课程预约的确定按钮
    def confirm_delete_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element

    def delete_success_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element




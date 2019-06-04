'''
coding=utf-8
Tina 2018-08-20
团课课表的页面封装
'''
from util.object_map import *
from util.opeartion_json import OperetionJson
from datetime import datetime


class GroupSchedule:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.opera_json = OperetionJson()


    # 进入左侧菜单——课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[4]/a/i')
        return element

    # 进入团课课表
    def go_group_schedule_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="团课课表"]')
        return element

    # 团课课表页面的“添加”按钮
    def add_group_schedule_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer add"]')
        return element

    # 添加团课课表的弹框中新增团课名称
    def add_course_store_obj(self):
        element = getElement(self.driver, 'name', 'shop_id')
        return element

    # 添加团课课表的弹框中新增场地
    def add_course_site_obj(self):
        element = getElement(self.driver, 'name', 'space_id')
        return element

    # 添加团课课表的弹框中时间
    def add_course_time_obj(self):
        element = getElement(self.driver,'name','time_from')
        return element

    # 添加团课课表的弹框中当天的课程
    def select_course_store_obj(self,weekday):
        element = getElement(self.driver, 'xpath', '//select[@name="course_cat_id" and @data="{}"]'.format(weekday))
        return element

    # 添加团课课表的弹框中当天上课的教练
    def select_course_coach_obj(self,coach_id):
        element = getElement(self.driver, 'name', '{}'.format(coach_id))
        return element

    # 确认按钮
    def add_confirm_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element

    # 团课课表的门店下拉框的选择
    def select_store_obj(self):
        element = getElement(self.driver,'xpath','//select[@class="select-1 shop_list"]/option[text()="懒猫馆——测试数据不能删除"]')
        return element

    # 选择要操作的团课课表(免费的)
    def select_course_obj(self,class_schedule):
        element = getElement(self.driver,'xpath','//span[text()="{}"]'.format(class_schedule))
        return element


    # 团课课表的查看按钮
    def view_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer info"]')
        return element

    # 团课课表详情页的添加团课预约
    def appoint_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="添加团课预约"]')
        return element

    # 添加团课预约输入手机号
    def member_phone_obj(self):
        element = getElement(self.driver,'xpath','//input[@name="se"]')
        return element

    # 筛选会员：“测试数据不要删除(18321829313)”
    def search_customer_obj(self):
        element = getElement(self.driver, 'xpath','//ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content"]//li[text()="测试数据不要删除(18321829313)"]')
        return element

    # 选择会员的储值卡预约团课
    def select_card_obj(self):
        element = getElement(self.driver,'xpath','//label[contains(text(),"储值卡不要删除数据")]//preceding-sibling::input')
        return element

    # 添加团课预约页面的确认按钮
    def group_appoint_confirm_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element

    # 预约成功后的弹框确认
    def group_script_confirm_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="lay-btn-confirm"]')
        return element


    # 团课课表详情页的取消预约按钮
    def cancel_appointment_obj(self):
        element = getElement(self.driver,'xpath','//table[@class="table-1 order_list"]//td[text()="18321829313"]/following-sibling::td//a[text()="取消预约"]')
        return element

    # 取消的确认按钮
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element

    # 取消预约成功提示按钮
    def cancel_success_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element

    # 返回团课列表
    def return_list_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="< 返回团课列表"]')
        return element

    # 删除课表
    def delete_button_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer del"]')
        return element

    # 浏览器自带弹框弹框确认
    def confirm_obj(self):
        self.driver.switch_to_alert().accept()

    # 新增排课成功后的确认按钮
    def course_schedule_confirm_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element













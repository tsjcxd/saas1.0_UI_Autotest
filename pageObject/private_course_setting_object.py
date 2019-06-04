'''
coding=utf-8
Tina 2018-08-20
私教课程设置页面：
1.私教课程添加页面（弹屏）
2.私教课程储值卡付费设置（弹屏）
3.私教课程价格设定的页面的封装（为会员购买私教合同使用）
'''
from util.object_map import *

class PrivateCourseSetting:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    # 页面一：私教课程添加页面（弹屏）
    # 左侧菜单：课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[4]/a/i')
        return element

    # 切换至私教课程设置的Table
    def go_private_course_setting_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="私教课程设置"]')
        return element

    # 添加私教课程的按钮
    def add_private_course_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="columns-13 right"]/i[1]')
        return element

    # 添加课程名字
    def add_course_name_obj(self):
        element = getElement(self.driver,'name','name')
        return element

    # 添加课程时间
    def add_course_time_obj(self):
        element = getElement(self.driver,'name','course_minutes')
        return element

    # 选择可售卖门店
    def add_course_store_obj(self):
        element = getElement(self.driver, 'xpath', '//label[contains(text(),"懒猫馆——测试数据不能删除")]')
        return element

    # 选择可预约的上课教练
    def add_course_coach_obj(self):
        element = getElement(self.driver, 'xpath', '//label[contains(text(),"测试教练不要删除")]')
        return element

    # 支持储值卡购买
    def add_card_obj(self):
        element = getElement(self.driver,'id','fee_type_1')
        return element

    # 确认
    def add_confirm_obj(self):
        element = getElement(self.driver, 'xpath', '//a[@class="btn-small save"]')
        return element

    # 确认信息框
    def prompt_message_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a')
        return element




    # 私教课程删除按钮
    def delete_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="columns-5 course_cat_list"]//i[@class="icon_club pointer del"]')
        return element

    # 私教课程删除的确认按钮
    def confirm_delete_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element

    # 私教课程删除成功的提示按钮
    def cancel_success_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[text()="确定"]')
        return element

    # 页面二：私教课程储值卡付费设置（弹屏）
    # 左侧菜单：课程

    # 选择付费设置的第一个私教课程
    def select_firse_course_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="course_list"]/p[1]')
        return element

    # 选择付费设置的私教课程
    def select_course_obj(self,course_name):
        element = getElement(self.driver,'xpath','//div[@class="course_list"]//p[contains(text(),"{}")]'.format(course_name))
        return element

    # 定位付费按钮
    def pay_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer pay_coach hastip"]')
        return element


    # 私教付费选择储值卡
    def select_card_obj(self):
        element = getElement(self.driver, 'xpath', '//td[text()="储值卡不要删除数据"]/preceding-sibling::td[1]//input')
        return element

    # 私教付费输入设置的金额
    def money_setting_obj(self):
        element = getElement(self.driver, 'xpath', '//td[text()="储值卡不要删除数据"]/following-sibling::td[1]//input')
        return element

    # 保存
    def save_card_button_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="确定"]')
        return element

    # 确认
    def confirm_card_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[@class="lay-btn-confirm"]')
        return element


    # 页面三：私教课程价格设定的页面的封装（为会员购买私教合同使用）
    # 定位私教课程
    # def select_PrivateCourseObj(self):
    #     element = getElement(self.driver,'xpath','//div[@class="course_list"]//p[contains(text(),"私教课程自动化测试不允许删除 | 储值卡单次可买")]')
    #     return element

    # 添加
    def add_private_course_price_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="columns-8 right"]/i[1]')
        return element

    # 输入数量区间的开始值
    def add_number_from_obj(self):
        element =  getElement(self.driver,'name','number_from')
        return element

    # 输入数量区间的结束值
    def add_number_to_obj(self):
        element = getElement(self.driver,'name','number_to')
        return element

    # 输入售价
    def add_price_obj(self):
        element = getElement(self.driver,'name','price')
        return element

    # 输入转让的百分比
    def add_fee_obj(self):
        element = getElement(self.driver,'name','fee')
        return element

    # 保存
    def save_price_button_obj(self):
        element = getElement(self.driver,'xpath','//a[@class="btn-small save"]')
        return element

    # 确认
    def confirm_price_button_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="lay-body lay-msg"]//a[@class="lay-btn-confirm"]')
        return element

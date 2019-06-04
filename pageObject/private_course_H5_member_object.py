'''
coding=utf-8
Tina 2018-09-03
会员端预约私教课程页面的封装
'''
from util.object_map import *
from util.opeartion_json import OperetionJson
class PrivateCourse_H5Member:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.opera_json=OperetionJson()

    # 切换至底部的课程
    def go_course_table_obj(self):
        element = getElement(self.driver,'xpath','//li[@class="course"]//span[text()="课程"]')
        return element

    # 定位右上角私教table
    def private_course_table_obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="tab"]/li[2]')
        return element

    # 定位场馆
    def store_select_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="shop_show"]')
        return element

    def store_select1_Obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="shop_content"]//li[@data="369627602"]')
        return element

    # 私教课程列表
    def appoint_obj(self):
        element = getElement(self.driver, 'xpath','//ul[@class="coach_class"]/li[@class="each"]/a[1]/div/h3[text()="{}"]'.format(self.opera_json.get_data("test01_add_private_course")))
        return element

    # 私教课程详情页面预约
    def appoint_detail_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="立即预约"]')
        return element

    # 预约时间
    def appointment_time_obj(self):
        element = getElement(self.driver,'xpath','//div[@class="course_info r"]/ul/li[4]/a')
        return element

    # 选择时间：22:30
    def specific_time_obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="choose_time"]/li[1]')
        return element

    # 确认时间
    def confirm_time_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确认"]')
        return element

    # 确认预约
    def confirm_appoint_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="确认预约"]')
        return element

    # 浏览器弹框确认
    def confirm_obj(self):
        self.driver.switch_to_alert().accept()


'''
coding=utf-8
Tina 2018-08-22
员工列表页面的元素的封装
'''

from util.object_map import *
class StaffList:
    def __init__(self,driver):
        self.driver =driver
        self.driver.implicitly_wait(30)

    # 左侧菜单栏：员工
    def go_staff_page_obj(self):
        element = getElement(self.driver, 'xpath', '/html/body/div[1]/div[1]/div[1]/ul/div[1]/div/li[6]/a/i')
        return element

    # 选择要删除的数据
    def data_selected_obj(self,nickname):
        element = getElement(self.driver,'xpath','//table[@class="table-1 edit-mode"]//td[text()="{}"]'.format(nickname))
        return element

    # 右上角的删除按钮
    def delete_button_obj(self):
        element = getElement(self.driver,'xpath','//i[@class="icon_club pointer del"]')
        return element

    # 浏览器弹框确认
    def confirm_obj(self):
        self.driver.switch_to_alert().accept()

    # 删除成功提示
    def delete_success_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element


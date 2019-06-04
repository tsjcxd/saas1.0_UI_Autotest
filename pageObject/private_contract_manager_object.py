'''
coding=utf-8
User:Tina
data:2018-08-22
编辑私教合同有效期页面元素的封装
'''
from util.object_map import *
from selenium.webdriver.common.action_chains import ActionChains


class PrivateContractManager():
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)



    def go_purchase_menu_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[5]/a/i')
        return element

    def go_private_contract_manager(self):
        element = getElement(self.driver,'xpath','//a[text()="私教合同管理"]')
        return element

    # 选择门店
    def select_store_obj(self):
        element = getElement(self.driver,'name','shop_id')
        return element

    # 搜索
    def search_obj(self):
        element = getElement(self.driver,'xpath','//input[@value="搜索"]')
        return element

    #  选择修改合同有效期的私教合同
    def select_contract_obj(self):
        element = getElement(self.driver,'xpath','//table[@class="table-1 edit-mode"]/tbody/tr[1]')
        return element

    # 选择“更多”
    def more_menu_obj(self):
        article= self.driver.find_element_by_link_text(u'更多')
        ActionChains(self.driver).move_to_element(article).perform()

    # 选择“更多”的修改合同有效期
    def edit_validity_period_obj(self):
        element = getElement(self.driver,'xpath','//ul[@class="dropdown-menu hide"]//a[text()="修改合同有效期"]')
        return element

    # 修改合同的开始时间
    def time_from_obj(self):
        element = getElement(self.driver,'name','valid_from')
        return element

    # 修改合同的结束时间
    def time_to_obj(self):
        element = getElement(self.driver,'name','valid_to')
        return element

    # 输入备注
    def note_obj(self):
        element = getElement(self.driver,'name','note')
        return element

    # 确定
    def confirm_button_obj(self):
        element = getElement(self.driver,'xpath','//button[text()="确定"]')
        return element

    # 弹框确定
    def bullet_box_confirm(self):
        element = getElement(self.driver,'xpath','//a[text()="确定"]')
        return element



if __name__ == '__main__':

    from selenium import webdriver
    from appModules.login_action import LoginAction
    driver = webdriver.Chrome(executable_path=r"D:\STYD\unittest_club\driver\chromedriver.exe")
    driver.get("http://www.styd.cn/")
    driver.maximize_window()
    LoginAction.login(driver,"18589091046","stydchange42018")

    PrivateContract = PrivateContractManager(driver)
    PrivateContract.go_purchase_menuObj().click()






'''
coding=utf-8
User:Tina
data:2018-08-22
储值卡有效期编辑页面元素的封装
'''

from util.object_map import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class CardContractManager:

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)



    #左侧菜单栏：售卖
    def go_purhase_obj(self):
        element = getElement(self.driver,'xpath','//*[@id="mCSB_1_container"]/li[5]/a/i')
        return element

    # 切换至储值卡合同管理
    def card_contarct_manager_obj(self):
        element = getElement(self.driver,'xpath','//a[text()="储值卡合同管理"]')
        return element

    # 选择门店
    def select_store_obj(self):
        element = getElement(self.driver,'name','shop_id')
        return element

    # 搜索
    def search_obj(self):
        element = getElement(self.driver,'xpath','//input[@value="搜索"]')
        return element

    #  选择修改合同有效期的储值卡合同
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



# #单元测试
# if __name__ == '__main__':
#     from selenium import webdriver
#     from pageObject.LoginPage_Object import LoginPage
#     import time
#     driver = webdriver.Chrome(
#         executable_path=r"D:\STYD\unittest_club\driver\chromedriver.exe")
#     driver.get("http://www.styd.cn/")
#     driver.maximize_window()
#     login = LoginPage(driver)
#     login.loginNameObj().click()
#     login.userNameObj().send_keys('18589091046')
#     login.passWordObj().send_keys('stydchange42018')
#     login.loginButton().click()
#     time.sleep(3)
#     CardContract = CardContractManager(driver)
#     CardContract.go_PurhaseObj().click()
#     time.sleep(2)
#     CardContract.CardContarct_ManagerObj().click()
#     time.sleep(2)
#     Select(CardContract.SelectStore_Obj()).select_by_visible_text("懒猫馆——测试数据不能删除")
#     CardContract.Search_Obj().click()
#     time.sleep(2)
#     CardContract.SelectContract_Obj().click()
#     time.sleep(2)
#     CardContract.MoreMenu_Obj()
#     time.sleep(2)
#     CardContract.EditValidityPeriod_Obj().click()
#     time.sleep(2)
#     CardContract.TimeFrom_Obj().send_keys("2018-09-01")
#     CardContract.TimeTo_Obj().send_keys("2018-09-05")
#     CardContract.Note_Obj().send_keys("自动化修改合同的有效期")
#     CardContract.ConfirmButtonObj().click()
#     CardContract.BulletBoxConfirm().click()
#
#     driver.quit()



'''
coding=utf-8
User:Tina
data:2018-08-22
添加:储值卡设置
'''

from pageObject.add_store_card_object import AddStoreCard
import time


class StoreCardSetting:

    def __init__(self):
        print("添加储值卡的设置")

    @staticmethod
    def card_setting(driver,cardname):
        addcardsetting = AddStoreCard(driver)
        driver.implicitly_wait(30)


        #进入左侧的菜单：购买
        addcardsetting.go_purchase_menu_obj().click()

        #切换至菜单：储值卡设置
        addcardsetting.go_store_card_setting_obj().click()

        #添加
        addcardsetting.add_card_obj().click()
        time.sleep(2)


        #卡名称
        addcardsetting.name_obj().send_keys(cardname)

        #有效期
        addcardsetting.valid_days_obj().send_keys(1000)

        #售卖基础价格
        addcardsetting.price_obj().send_keys(10)

        #实际价值
        addcardsetting.real_price_obj().send_keys(1000)

        #转让手续费
        addcardsetting.fee_obj().send_keys(1)

        #门店
        addcardsetting.shop_select_obj().click()

        #支持消费方式
        addcardsetting.consumption_patterns1().click()
        addcardsetting.consumption_patterns2().click()
        addcardsetting.consumption_patterns3().click()
        addcardsetting.consumption_patterns4().click()

        #售卖时间
        addcardsetting.sale_time_from_obj().send_keys("2018-10-17")
        addcardsetting.sale_time_to_obj().send_keys("2019-12-17")
        time.sleep(2)

        #可在线购买
        addcardsetting.purchase_obj().click()
        time.sleep(2)

        #设置权重
        addcardsetting.weights_obj().send_keys(10)
        time.sleep(3)

        #保存
        addcardsetting.confirm_obj().click()
        time.sleep(2)

        # 确认
        addcardsetting.confirm_button_obj().click()

        # 切换至菜单：储值卡设置
        addcardsetting.go_store_card_setting_obj().click()








'''
封装共用的函数：
检查新增是否成功
'''



class CheckData:
    @classmethod
    def check_data(self,driver,path,except_value,parameter):
        table = driver.find_element_by_xpath(path)
        rows = table.find_elements_by_tag_name("tr")
        contenttexts = [row.find_element_by_xpath("td[{}]".format(parameter)) for row in rows[1:]]
        texts = [coll.text for coll in contenttexts]
        assert except_value in texts, "this is except_value : ...{}...,\n this is texts : ...{}...".format(except_value,texts)
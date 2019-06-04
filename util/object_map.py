from selenium.webdriver.support.ui import WebDriverWait

def getElement(driver, locateType, locateExpression):
    element = WebDriverWait(driver,30).until(lambda x: x.find_element(by = locateType,value= locateExpression))
    return element

def getElements(driver, locateType, locateExpression):
    elements = WebDriverWait(driver,30).until(lambda x: x.find_element(by = locateType,value= locateExpression))
    return elements

def getElementByText(driver, link_text):
    element = driver.find_element_by_link_text(link_text)
    return element


def getElementsByText(driver, text):
    elements = driver.find_element_by_link_text(text)
    return elements


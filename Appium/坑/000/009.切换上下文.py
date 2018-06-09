#coding=utf-8
from appium import webdriver

desired_caps = {}

desired_caps = {
'platformName': 'Android',
'platformVersion': '4.4.2',
'deviceName': 'Android Emulator',
'browserName': 'Browser',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print ("start baidu page!")

driver.get('https://www.baidu.com')

#获取当前上下文
cct = driver.current_context
print (cct)

#切换为 web
#driver.switch_to.context('WEBVIEW_1')

driver.find_element_by_id("kw").send_keys("appium")

driver.find_element_by_id("su").click()

driver.quit()
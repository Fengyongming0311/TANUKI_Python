from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = Remote(command_executor = 'http://127.0.0.1:4444/wd/hub',
		desired_capabilities = {'platform': 'ANY',
							'browserName':'chrome',
							'version': '',
							'javascriptEnabled': True
							})






'''
'platform': 'ANY' 平台默认可以是任何（Windows，MAC，android）。
'browserName': 'chrome' 浏览器名字是 chrome。
'version': '' 浏览器的版本默认为空。
'javascriptEnabled': True javascript 启动状态为 True。
'''
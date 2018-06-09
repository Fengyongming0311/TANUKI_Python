# Android environment

from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


'''
Appium 的 Desired Capabilities 是扩展了 webdriver 的 Desired Capabilities 的。
automationName：使用哪种自动化引擎。appium（默认）还是 Selendroid ??
platformName：使用哪种移动平台。iOS, Android, orFirefoxOS？
deviceName：启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhoneRetina 4-inch, Android Emulator, Galaxy S4, etc...
app：应用的绝对路径，注意一定是绝对路径。如果指定了 appPackage 和 appActivity 的话，这个属性是可以不设置的。另外这个属性和 browserName 属性是冲突的。
browserName：移动浏览器的名称。比如 Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android；与 app 属性互斥。
udid：物理机的 id。比如 1ae203187fc012g。(UDID 是由子母和数字组成的字符串的序号，用来区别每一个唯一的 Android/iOS 设备。)
'''
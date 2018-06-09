__author__ = 'TANUKI'
# -*- coding: utf-8 -*-
#手机Appium配置
import sys
sys.path.append("..")



def iPhone6():
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '11.2'
    desired_caps['udid'] = '662ec68d7cb948a8c15de13db97f432d30b467b5'
    #desired_caps['automationName'] = "uiautomator2"
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    desired_caps['deviceName'] = '冯泳铭的 iPhone'
    desired_caps['bundleId'] = 'pujiHachiApp.com'
    #desired_caps['automationName'] = 'XCUITest'
    desired_caps['noSign'] = 'True'
    #跳过检查和对应用进行 debug 签名的步骤。只能在使用 UiAutomator 时使用，使用 selendroid 是不行。默认值 false
    return desired_caps


#VIVO_X9手机
def VIVO_X9():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['automationName'] = "uiautomator2"
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'  # vivo Y51A
    #desired_caps['unicodeKeyboard'] = 'True'
    #使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #desired_caps['resetKeyboard'] = 'True'
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    desired_caps['noSign'] = 'True'
    #跳过检查和对应用进行 debug 签名的步骤。只能在使用 UiAutomator 时使用，使用 selendroid 是不行。默认值 false
    return desired_caps



def huawei_NOT8():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    #desired_caps['platformVersion'] = '7.1.1'
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    #desired_caps['app'] = XXXXXXX  # 测试apk包
    desired_caps['deviceName'] = 'huawei-edi_al10-8DF6R16B07000761'  # vivo Y51A
    #desired_caps['unxcodeKeyboard'] = 'True'
    #不知道是干嘛的先屏蔽掉
    desired_caps['resetKeyboard'] = 'True'
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    desired_caps['unicodeKeyboard'] = 'True'
    #使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    #desired_caps['appWaitActivity'] =.ui.startup.role.RoleActivity
    #desired_caps['recreateChromeDriverSessions'] = 'True'
    return desired_caps


def huawei_P9():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    #desired_caps['app'] = XXXXXXX  # 测试apk包
    desired_caps['deviceName'] = 'huawei-eva_al00-PBV0216526003556'  #P9
    # #desired_caps['unxcodeKeyboard'] = 'True'
    #不知道是干嘛的先屏蔽掉
    desired_caps['resetKeyboard'] = 'True'
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    desired_caps['unicodeKeyboard'] = 'True'
    #使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    #desired_caps['appWaitActivity'] =.ui.startup.role.RoleActivity
    #desired_caps['recreateChromeDriverSessions'] = 'True'
    return desired_caps


def hw_honor_P9():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    #desired_caps['app'] = XXXXXXX  # 测试apk包
    desired_caps['deviceName'] = 'huawei-duk_al20-FFK0217609003306'  #V9
    # #desired_caps['unxcodeKeyboard'] = 'True'
    #不知道是干嘛的先屏蔽掉
    desired_caps['resetKeyboard'] = 'True'
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    desired_caps['unicodeKeyboard'] = 'True'
    #使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    #desired_caps['appWaitActivity'] =.ui.startup.role.RoleActivity
    #desired_caps['recreateChromeDriverSessions'] = 'True'
    return desired_caps




#VIVO_X9手机包含测试注释代码
def VIVO_TEST():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    #desired_caps['platformVersion'] = '7.1.1'
    #desired_caps['automationName'] = 'Selendroid'
    desired_caps['automationName'] = "uiautomator2"
    #desired_caps['aut'] = 'io.selendroid.testapp:0.17.0'
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    #desired_caps['app'] = XXXXXXX  # 测试apk包
    desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'  # vivo Y51A
    #desired_caps['unxcodeKeyboard'] = 'True'
    #不知道是干嘛的先屏蔽掉
    #desired_caps['unicodeKeyboard'] = 'True'
    #使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #desired_caps['resetKeyboard'] = 'True'
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    #如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['noSign'] = 'True'
    #跳过检查和对应用进行 debug 签名的步骤。只能在使用 UiAutomator 时使用，使用 selendroid 是不行。默认值 false
    #desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.main.views.activities.MainActivity'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    #desired_caps['appWaitActivity'] = ".modules.wallet.views.activitys.MyWalletActivity"
    #会一直等待这个activity


    #desired_caps['enablePerformanceLogging'] = 'True'
    #(仅适用于 Chrome 和 webview) 开启 Chromedriver 的性能日志。 (默认 false)

    return desired_caps

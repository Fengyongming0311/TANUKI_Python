__author__ = 'TANUKI'
# -*- coding: utf-8 -*-
#手机Appium配置
import sys
sys.path.append("..")


#VIVO_X9手机
def VIVO():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    #desired_caps['platformVersion'] = '7.1.1'
    desired_caps['noReset'] = True  # 不需要每次都安装apk
    #desired_caps['app'] = XXXXXXX  # 测试apk包
    desired_caps['deviceName'] = 'vivo-vivo_x9-be1bd33f'  # vivo Y51A
    #desired_caps['unxcodeKeyboard'] = 'True'
    #不知道是干嘛的先屏蔽掉
    desired_caps['resetKeyboard'] = 'True'
    #'unicodeKeyboard':True,#使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
    #'resetKeyboard':True #隐藏虚拟键盘，防止遮挡元素
    #不知道是干嘛的先屏蔽掉
    #如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps['appPackage'] = 'com.pujitech.pujiejia'
    desired_caps['appActivity'] = 'com.pujitech.pujiejia.modules.splash.views.activities.SplashActivity'
    #desired_caps['appWaitActivity'] =.ui.startup.role.RoleActivity
    return desired_caps


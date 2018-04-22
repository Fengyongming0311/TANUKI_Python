__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time

###
import sys
sys.path.append("..")
import huadong
###

class MyHome:
    def MyHome_one(driver):
        '''
        先点击我家按钮进入首页页面
        '''
        tab = "我家"
        try:
            time.sleep(3)
            allbutn = driver.find_elements_by_id("com.pujitech.pujiejia:id/fixed_bottom_navigation_title")
            for target in allbutn:
                if target.text == tab:
                    target.click()
                    break
                #点完了就跳出循环，否则会再次找寻case内容导致报错
        except:
            print ("未切换到我家页面，程序退出....")
            quit()

    ##################下面是正式的测试代码####################
    #进入我的消息页面和设置页面查看页面是否正确显示
    #修改用户个人资料
    def MyHome_two(driver):
        try:
            time.sleep(3)
            case = "我的消息"
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_message").click()

            time.sleep(3)
            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)




        #进入设置页面查看页面是否正确显示
        try:
            time.sleep(3)
            case = "设置"
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_setting").click()


            time.sleep(3)
            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击%s用例Passed............成功"%case)
        except:
            print ("测试点击%s用例失败............Failed"%case)



        #点击头像图片进入个人资料页面
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)

            case = "个人资料"
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_avatar").click()

            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击头像图片进入%s用例Passed............成功"%case)
        except:
            print ("测试点击头像图片进入%s用例失败............Failed"%case)


        #点击用户名称进入个人资料页面
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            case = "个人资料"
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_name").click()

            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                driver.back()

            print ("测试点击用户名称进入%s用例Passed............成功"%case)
        except:
            print ("测试点击用户名称进入%s用例失败............Failed"%case)


        #点击用户手机号进入个人资料页面
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            case = "个人资料"
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_phone").click()

            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)

            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == case:
                print ("测试点击用户手机号进入%s用例Passed............成功"%case)
                into = True



        except:
            print ("测试点击用户手机号进入%s用例失败............Failed"%case)
            into = False


        #测试修改个人用户信息当into为true开始如下用例
        #case01：修改用户头像
        if into == True:
            try:
                #点相机
                driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
                #等待
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_self_info_avatar").click()
                #点击头像

                time.sleep(2)
                #点相机com.pujitech.pujiejia:id/tv_camera
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_camera").click()

                driver.wait_activity(".CameraActivity", 30)
                #等待进入照相功能

                driver.back()

                #点相册
                driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
                #等待回到个人资料页面
                driver.find_element_by_id("com.pujitech.pujiejia:id/iv_self_info_avatar").click()
                #点击头像

                time.sleep(2)
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_gallery").click()
                #点相册com.pujitech.pujiejia:id/tv_gallery

                driver.wait_activity("com.android.gallery3d.app.Gallery", 30)
                #点击相册名称进去选图片
                driver.find_element_by_android_uiautomator('new UiSelector().text("相机")').click()

                time.sleep(3)
                driver.wait_activity("com.android.gallery3d.vivo.NewPageActivity", 30)
                driver.tap([(145,330)], 500)
                #点击第一张相片145，330

                time.sleep(3)
                driver.wait_activity("com.android.gallery3d.app.CropImage", 30)
                aru = driver.find_elements_by_class_name("android.widget.Button")
                for timme in aru:
                    if timme.text == "确定":
                        timme.click()
                        break

                print ("测试修改用户头像用例Passed............成功")
            except:
                print ("测试修改用户头像用例失败............Failed")
                pass





            #修改昵称为...大妈的狂笑
            #修改性别如果名字叫大妈的狂笑则为女性，如果是蒜泥晾衣白肉则为男性
            try:
                time.sleep(3)
                name1 = "大妈的狂笑"
                name2 = "蒜泥晾衣白肉"

                nickname = driver.find_element_by_id("com.pujitech.pujiejia:id/et_self_info_nickname")

                if nickname.text == name1:
                    nickname.click()
                    nickname.clear()
                    nickname.send_keys(name2)
                    print ("测试修改昵称为%s用例Passed............成功"%name2)
                elif nickname.text == name2:
                    nickname.click()
                    nickname.clear()
                    nickname.send_keys(name1)
                    print ("测试修改昵称为%s用例Passed............成功"%name1)
                elif nickname != name1 and nickname != name2:
                    nickname.click()
                    nickname.clear()
                    nickname.send_keys(name1)
                    print ("测试修改昵称为%s用例Passed............成功"%name1)
            except:
                print ("测试修改用户昵称用例失败............Failed")


            #修改用户的性别
            time.sleep(2)
            try:
                nickname = driver.find_element_by_id("com.pujitech.pujiejia:id/et_self_info_nickname")
                if nickname.text == name1:
                    driver.find_element_by_id("com.pujitech.pujiejia:id/rb_female").click()
                elif nickname.text == name2:
                    driver.find_element_by_id("com.pujitech.pujiejia:id/rb_male").click()

                print ("测试修改用户的性别用例Passed............成功")
            except:
                print ("测试修改用户的性别用例失败............Failed")



            #修改用户生日信息不可操错
            #修改用户身高不可操作
            #修改用户体重不可操作
            #点击保存按钮
            try:
                driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
                driver.find_element_by_id("com.pujitech.pujiejia:id/btn_save_self_info").click()
                print ("测试保存修改的个人资料信息用例Passed............成功")
            except:
                print ("测试保存修改的个人资料信息用例失败............Failed")

    #地址管理
    #我的钱包，点击充值然后返回，点击更多明细返回，点击余额说明返回
    #我的优惠券
    def MyHome_three(driver):
        #进入地址管理
        #页面无法使用任何定位方式定位元素
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            driver.find_element_by_id("com.pujitech.pujiejia:id/ll_address_manager_container").click()
            #点击进入地址管理

            #driver.back()

            #bak = driver.current_url
            #print (bak)

            print ("========================")
            time.sleep(5)

            driver.tap([(550,600)], 500)

            time.sleep(3)
            ct = driver.contexts
            print ("ct===",ct)

            driver.switch_to.context('WEBVIEW_com.pujitech.pujiejia')

            time.sleep(2)

            dondake = driver.find_elements_by_xpath("//*")
            for i in dondake:
                print (i)
                print (i.text)

            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_add_address").click()



            print ("测试进入地址管理用例Passed............成功")
        except:
            print ("测试进入地址管理用例失败............Failed")
            pass







__author__ = 'TANUKI'
#coding:utf-8
from appium import webdriver
import time
###
import sys
sys.path.append("..")
from FilePublic_Page import Public_Page
import huadong
import random
###

class MyHome:
    def IntoMyHome(driver):
        """
        点击我家按钮进入我家页面
        """
        Public_Page.Switch_Navigation(driver, tab="我家")

    def IntoDengLuPage(driver):
        """
        从我家页面未登录任何账户进入登录页面
        :return: None
        """
        time.sleep(2)
        MyHome.IntoMyHome(driver)
        time.sleep(3)
        userinfo = driver.find_element_by_id('com.pujitech.pujiejia:id/tv_user_center_name')
        if userinfo.text == "未登录":
            userinfo.click()


    ##################下面是正式的测试代码####################
    #进入我的消息页面和设置页面查看页面是否正确显示
    #修改用户个人资料
    def MyHome_two(driver):
        #测试我的消息页面是否正常显示
        Public_Page.NomalTest(driver, title = "我的消息",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/iv_message",
                              Wait_Element = ".modules.h5.views.activitys.CommonH5Activity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title"
                              )

        #测试设置页面是否正确显示
        Public_Page.NomalTest(driver, title = "设置",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/iv_setting",
                              Wait_Element = ".modules.usercenter.setting.views.activities.SettingActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title"
                              )

        #点击头像图片进入个人资料页面
        Public_Page.NomalTest(driver, title = "个人资料",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/iv_avatar",
                              Wait_Element = ".modules.usercenter.selfinfo.views.activities.SelfInfoActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title"
                              )

        #点击用户名称进入个人资料页面
        Public_Page.NomalTest(driver, title = "个人资料",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/tv_user_center_name",
                              Wait_Element = ".modules.usercenter.selfinfo.views.activities.SelfInfoActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title"
                              )

        #点击用户手机号进入个人资料页面
        Public_Page.NomalTest(driver, title = "个人资料",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/tv_user_center_phone",
                              Wait_Element = ".modules.usercenter.selfinfo.views.activities.SelfInfoActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title"
                              )

        #点击用户手机号进入个人资料页面，并修改个人资料数据

    #修改个人头像功能
    def Change_ProfilePhoto(driver):
        '''
        修改个人头像功能
        先决条件：已经进入我家页面
        :return: None
        '''
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            # 等待我家主界面activity
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_name").click()
            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
            time.sleep(1)
            checkpoint = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_title")
            if checkpoint.text == "个人资料":
                #case:修改用户头像
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
                    time.sleep(3)
                    driver.back()
                    # 等待进入照相功能,进入后等待3s后退出

                    driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
                    #等待回到个人资料页面

                    driver.find_element_by_id("com.pujitech.pujiejia:id/iv_self_info_avatar").click()
                    #点击头像
                    time.sleep(2)
                    driver.find_element_by_id("com.pujitech.pujiejia:id/tv_gallery").click()
                    #点相册com.pujitech.pujiejia:id/tv_gallery

                    driver.wait_activity("com.android.gallery3d.app.Gallery", 30)
                    time.sleep(3)
                    #点击相册名称进去选图片
                    driver.find_element_by_android_uiautomator('new UiSelector().text("相机")').click()

                    #driver.wait_activity("com.android.gallery3d.vivo.NewPageActivity", 30)
                    time.sleep(3)
                    driver.tap([(135, 345)])
                    #driver.tap([(135, 345)], 500)加了后边的500变成了持续长按
                    #点击第一张相片
                    driver.wait_activity("com.android.gallery3d.app.CropImage", 30)
                    time.sleep(3)
                    aru = driver.find_elements_by_class_name("android.widget.Button")
                    for timme in aru:
                        if timme.text == "确定":
                            timme.click()
                            break
                    time.sleep(2)
                    print("测试修改用户头像用例Passed............成功")
                except:
                    print("测试修改用户头像用例失败............Failed")
                    pass
        except:
            print("测试修改用户头像用例失败............Failed")
            pass

    def Change_PersonalData(driver):
        '''
        修改个人资料功能
        先决条件：已经进入我家页面
        :return: None
        '''
        #修改昵称
        #修改性别如果名字叫大妈的狂笑则为女性，如果是蒜泥晾衣白肉则为男性
        try:
            '''
            #如果修改完头像后直接进入这个页面，那么不用点击名字进入个人资料页
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            # 等待我家主界面activity
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_user_center_name").click()
            '''
            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
            time.sleep(3)
            name1 = "茹香的小棉袄"
            name2 = "蒜泥晾衣白肉"

            nickname = driver.find_element_by_id("com.pujitech.pujiejia:id/et_self_info_nickname")

            if nickname.text == name1:
                nickname.click()
                nickname.clear()
                nickname.send_keys(name2)
                print("测试修改昵称为%s用例Passed............成功" % name2)
            elif nickname.text == name2:
                nickname.click()
                nickname.clear()
                nickname.send_keys(name1)
                print("测试修改昵称为%s用例Passed............成功" % name1)
            elif nickname != name1 and nickname != name2:
                nickname.click()
                nickname.clear()
                nickname.send_keys(name1)
                print("测试修改昵称为%s用例Passed............成功" % name1)
        except:
            print("测试修改用户昵称用例失败............Failed")

        # 修改用户的性别
        time.sleep(2)
        try:
            nickname = driver.find_element_by_id("com.pujitech.pujiejia:id/et_self_info_nickname")
            if nickname.text == name1:
                driver.find_element_by_id("com.pujitech.pujiejia:id/rb_female").click()
            elif nickname.text == name2:
                driver.find_element_by_id("com.pujitech.pujiejia:id/rb_male").click()

            print("测试修改用户的性别用例Passed............成功")
        except:
            print("测试修改用户的性别用例失败............Failed")

        # 修改用户生日信息
        """
        此滑动操作是以VivoX9屏幕大小选定的坐标，如若跑其他
        手机脚本无法滑动脚本报错，请修改适应其他手机脚本坐标
        """
        try:
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/rl_self_info_birthday_container").click()
            time.sleep(2)
            year = Public_Page.RandomNum()
            if year == 0:
                driver.swipe(150, 1625, 150, 1400)
                #上滑
            else:
                driver.swipe(150, 1625, 150, 1850)
                #下滑
            time.sleep(1)
            mouth = Public_Page.RandomNum()
            if mouth == 0:
                driver.swipe(540, 1625, 540, 1400)
                # 上滑
            else:
                driver.swipe(540, 1625, 540, 1850)
                # 下滑
            time.sleep(1)
            day = Public_Page.RandomNum()
            if day == 0:
                driver.swipe(900, 1625, 900, 1400)
                # 上滑
            else:
                driver.swipe(900, 1625, 900, 1850)
                # 下滑
            time.sleep(1)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
            time.sleep(2)
            print ("测试修改用户生日信息用例Passed............成功")
        except:
            print ("测试修改用户生日信息用例失败............Failed")
            pass
        # 修改用户身高
        try:
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/rl_self_info_height_container").click()
            time.sleep(2)
            num = Public_Page.RandomNum()
            if num == 0:
                driver.swipe(540, 1625, 540, 1400)
                #上滑
            else:
                driver.swipe(540, 1625, 540, 1850)
                #下滑
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
            time.sleep(2)
            print ("测试修改用户身高信息用例Passed............成功")
        except:
            print ("测试修改用户身高信息用例失败............Failed")
            pass

        # 修改用户体重不可操作
        try:
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/rl_self_info_weight_container").click()
            time.sleep(2)
            num = Public_Page.RandomNum()
            if num == 0:
                driver.swipe(540, 1625, 540, 1400)
                #上滑
            else:
                driver.swipe(540, 1625, 540, 1850)
                #下滑
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
            time.sleep(2)
            print ("测试修改用户体重信息用例Passed............成功")
        except:
            print ("测试修改用户体重信息用例失败............Failed")
            pass

        # 点击保存按钮
        try:
            driver.wait_activity(".modules.usercenter.selfinfo.views.activities.SelfInfoActivity", 30)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_save_self_info").click()
            print("测试保存修改的个人资料信息用例Passed............成功")
        except:
            print("测试保存修改的个人资料信息用例失败............Failed")

    '''
    #地址管理
    #我的钱包，点击充值然后返回，点击更多明细返回，点击余额说明返回
    #我的优惠券
    '''
    def AddressManage(driver):
        """
        先决条件：进入我家页面
        """
        #进入地址管理,进入新增地址
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            time.sleep(3)
            driver.find_element_by_id("com.pujitech.pujiejia:id/ll_address_manager_container").click()
            #点击地址管理

            driver.wait_activity(".modules.usercenter.address.views.activites.AddressManagerActivity", 30)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_add_address").click()
            #点击新增地址

            #通过方法AddAddress增加一条地址信息
            Contactname = MyHome.AddAddress(driver)

            allname = driver.find_elements_by_id("com.pujitech.pujiejia:id/tv_username")
            #获取所有姓名
            driver.wait_activity(".modules.usercenter.address.views.activites.AddressManagerActivity", 30)
            time.sleep(3)
            for i in allname:
                if i.text == Contactname:
                    print ("新增地址Succeeded....................................成功")
                    break
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            # 返回上一页面
        except:
            print("添加地址失败.....................................Failed")
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            # 返回上一页面


    def AddAddress(driver):
        """
        先决条件：进入
        """
        try:
            Contact = Public_Page.CrateName(1)[0]
            #联系人姓名
            driver.wait_activity(".modules.usercenter.address.views.activites.AddAddressActivity", 30)
            time.sleep(2)

            driver.find_element_by_id("com.pujitech.pujiejia:id/et_contact_username").send_keys("%s"%Contact)
            #输入联系人姓名
            time.sleep(3)

            driver.find_element_by_id("com.pujitech.pujiejia:id/et_contact_telephone").send_keys("%s"%Public_Page.CratePhoneNo(1)[0])
            time.sleep(3)

            address = "北京市朝阳区慧忠里%s号"%(random.randint(1000, 9999))

            inputmode = driver.find_element_by_id("com.pujitech.pujiejia:id/tv_input_mode")
            #print (inputmode.text)
            if inputmode.text == "手动输入地址":
                time.sleep(2)
                inputmode.click()

            time.sleep(3)
            driver.find_element_by_id("com.pujitech.pujiejia:id/et_detail_address").send_keys("%s"%address)
            #定位详细地址

            #time.sleep(2)
            #driver.tap([(988, 1132)])
            #隐藏键盘操作(VIVOX9)
            #988,1132

            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/btn_save_address").click()
            #点击保存com.pujitech.pujiejia:id/btn_save_address
            return Contact

        except:
            pass


    def DeleteAddress(driver, cishu):
        """
        先决条件：进入我家页面
        """
        try:
            driver.wait_activity(".modules.main.views.activities.MainActivity", 30)
            time.sleep(3)
            driver.find_element_by_id("com.pujitech.pujiejia:id/ll_address_manager_container").click()
            # 点击地址管理
            driver.wait_activity(".modules.usercenter.address.views.activites.AddressManagerActivity", 30)
            time.sleep(3)

            deletebtn = driver.find_elements_by_id("com.pujitech.pujiejia:id/ll_delete")
            #print (deletebtn[0])
            #print (deletebtn[1])
            #print (deletebtn[2])
            #print (deletebtn[3])
            for i in range(0, cishu):
                NoTwo = deletebtn[1]
                NoTwo.click()
                time.sleep(3)
                driver.find_element_by_id("com.pujitech.pujiejia:id/tv_confirm").click()
            print ("删除地址%s条Succeeded....................................成功"%cishu)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            #返回上一页面
        except:
            print("删除地址%s条失败.....................................Failed"%cishu)
            time.sleep(2)
            driver.find_element_by_id("com.pujitech.pujiejia:id/iv_back").click()
            #失败也返回上一页面


    def SmartBandInstruction(driver):
        """
        点击智能手环的使用说明
        先决条件：进入我家页面
        :return: None
        """
        Public_Page.NomalTest(driver, title = "使用说明",
                              MainWait_Element = ".modules.main.views.activities.MainActivity",
                              find_element_id = "com.pujitech.pujiejia:id/btn_brand_instruction",
                              Wait_Element = ".modules.help.view.activities.HelpActivity",
                              check_element_id = "com.pujitech.pujiejia:id/tv_title")













import uiautomator2 as u2

d = u2.connect_usb('be1bd33f')

import time

d(resourceId="com.bbk.launcher2:id/item_icon", className="android.widget.ImageView", instance=8).click()
time.sleep(5)

d(resourceId="com.pujitech.pujiejia:id/fixed_bottom_navigation_icon", description=u"icon", className="android.widget.ImageView", instance=3).click()

time.sleep(3)


d(resourceId="com.pujitech.pujiejia:id/tv_wallet").click()

time.sleep(3)


d(resourceId="com.pujitech.pujiejia:id/my_wallet_yue_shuoming_tv").click()

time.sleep(3)

d(resourceId="com.pujitech.pujiejia:id/iv_back").click()

time.sleep(3)

d(resourceId="com.pujitech.pujiejia:id/my_wallet_qu_chongzhi_btn").click()


time.sleep(3)

d(resourceId="com.pujitech.pujiejia:id/iv_back").click()
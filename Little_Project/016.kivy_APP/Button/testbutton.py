#coding:utf-8
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
#创建window
from kivy.utils import get_color_from_hex
#上显示背景色
from glob import glob
from os.path import dirname, join, basename
#做文件操作(上面俩)

name = (
	"莫永林",
	"王昊轩",
	"张娜",
	"刘雁辉",
	"冯泳铭")

for dondake in glob(join(dirname(__file__), '*.mp3')):
	print (dondake)


class Test(App):
	def build(self):
		#设置布局
		BUJU = BoxLayout()
		for name in Friends:
			#创建Button
			FriendsBTN = Button(text=name, font_name = '..\\Button\\ziti.ttf')
			BUJU.add_widget(FriendsBTN)
		return BUJU

	#def Soundname(self):


if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('00bfff')
	Test().run()

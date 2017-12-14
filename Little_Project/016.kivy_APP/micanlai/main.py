#coding:utf-8
'''
Audio example
=============

This example plays sounds of different formats. You should see a grid of
buttons labelled with filenames. Clicking on the buttons will play, or
restart, each sound. Not all sound formats will play on all platforms.

All the sounds are from the http://woolyss.com/chipmusic-samples.php
"THE FREESOUND PROJECT", Under Creative Commons Sampling Plus 1.0 License.

'''

import kivy
('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from glob import glob
from os.path import dirname, join, basename

# 点击按钮播放类AudioButton
class AudioButton(Button):
    #文件名
    filename = StringProperty(None)
    #声音
    sound = ObjectProperty(None, allownone=True)
    #音量调用了kivy中的NumericProperty
    volume = NumericProperty(1.0)
    #下点击后操作
    def on_press(self):
        #如果没播放，就播放点击按钮下的文件
        if self.sound is None:
            self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
        #如果状态不等于stop就stop他
        if self.sound.status != 'stop':
            self.sound.stop()
        #下声音大小
        self.sound.volume = self.volume
        #下真正播放？？
        self.sound.play()

    def release_audio(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None
    #控制声音大小
    def set_volume(self, volume):
        self.volume = volume
        if self.sound:
            self.sound.volume = volume

#AudioBackground
class AudioBackground(BoxLayout):
    pass


class AudioApp(App):

    def build(self):

        root = AudioBackground(spacing=5)
        for fn in glob(join(dirname(__file__), '*.wav')):
            btn = AudioButton(
                text=basename(fn[:-4]).replace('_', ' '), filename=fn,
                size_hint=(0.3, 0.2), halign='center',
                size=(12, 12), text_size=(118, None),
                font_name = 'ziti.ttf')
            root.ids.sl.add_widget(btn)

        return root

    def release_audio(self):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.release_audio()

    def set_volume(self, value):
        for audiobutton in self.root.ids.sl.children:
            audiobutton.set_volume(value)


if __name__ == '__main__':
    AudioApp().run()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Created on Tue Nov  6 01:18:45 2018
    * @par Copyright (C): 2010-2019, hunan CLB Tech
    * @file        speech-conpound
    * @version      V1.0
    * @details
    * @par History

    @author: zhulin
"""
from aip import AipSpeech
from time import time
import os

# import required modules
from pydub import AudioSegment
from pydub.playback import play

#通过百度云申请的账号和密码
baidu_APP_ID='42490250'
baidu_API_KEY='8vzlVs3CGsZpLiKNqtteZSKZ'
baidu_SECRET_KEY='kXpZDgCKRZGlKtZlOO4ZCFLiGBVYORHh'

baidu_aipSpeech=AipSpeech(baidu_APP_ID,baidu_API_KEY,baidu_SECRET_KEY)
#在可选的参数中对语速，音量，人声进行调整，这里采用‘per’为0的女生听起来会更清晰，因人而异！！！

# Open the file
with open('/home/pi/read.txt', 'r') as file:
    # Read the first line
    line = file.readline()
    # Split the line into words
    words = line.split()
    # Get the first word
    if words:
        mytext = words[0]

result = baidu_aipSpeech.synthesis(text = "Watch out!"+mytext+" detected",
                             options={'spd':5,'vol':100,'per':0,})
#将合成的语音保存为文件
if not isinstance(result,dict):
    with open('/home/pi/myread.mp3','wb') as f:
        f.write(result)

else:print(result)
#声音播放，我们可以利用树莓派自带的pygame软件
#pygame.mixer.init()
#pygame.mixer.music.load('/home/pi/CLBROBOT/makerobo.mp3')
#pygame.mixer.music.play()
# for playing mp3 file
song = AudioSegment.from_mp3('/home/pi/myread.mp3')
print('playing sound using  pydub')
play(song)

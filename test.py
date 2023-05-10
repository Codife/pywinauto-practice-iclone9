from pywinauto import Desktop, application, mouse
from pywinauto_recorder.player import *
import win32api
from threading import Timer
import time
import os
import librosa
from run import func
import shutil
import time


x = 0
frames_list = []
directory = './audios/'
mouse.click(button='left', coords=(1034, 533))
len = 0
for filename in os.listdir(directory):
    audio = os.path.join(directory, filename)
    if os.path.isfile(audio):
        name_audio = audio
        dur = librosa.get_duration(filename=name_audio)
        name_audio = name_audio.replace('./audios/', '')
        name_video = name_audio
        name_video = name_video.replace('./audios/', '')
        name_video = name_video.replace('.wav', '')
        frames = str(round(dur*30*2))
        try:
            start = time.time()
            print("Duration of Video: ", dur, " seconds")
            func(name_audio, mouse, double_click, time, mouse_wheel, double_left_click,
                 directory, os, librosa, send_keys, name_video, len, frames, find)
            len = len + 1
            end = time.time()
            print(end-start, "Seconds")
        except Exception as e:
            print(e)


# HUNAIN
# app = Application(backend="uia").start('Cal.exe')

# dlg.type_keys('2*3=')
# actionable_dlg = dlg['view'].wait('visible')
# dlg.minimize()
# Desktop(backend="uia").window('Calculator').restore()

# i = 69
# while i > 0:
#     x, y = win32api.GetCursorPos()
#     print(x, y)

# def pressApply():
# 	mouse.click(button='left', coords=(1393, 923))
# applyAudio.start()

# applyAudio = Timer(10.0, pressApply)


# mouse.click(button='left', coords=(1034, 533))
# mouse.click(button='left', coords=(192, 31))
# mouse.click(button='left', coords=(307 , 66))
# mouse.click(button='left', coords=(531, 133))
# mouse.click(button='left', coords=(1217, 474))
# mouse.click(button='left', coords=(911, 602))

# with UIPath(u"iClone||Window"):
# 	with UIPath(u"AccuLips||Window->Open||Window->||Pane->Shell Folder View||Pane->Items View||List->audios||ListItem"):
# 		double_click(u"Date modified||Edit")
# with UIPath(u"iClone||Window"):
# 	with UIPath(u"AccuLips||Window->Open||Window->||Pane->Shell Folder View||Pane->Items View||List->Be Sure To Look At The High Fly's!.wav||ListItem"):
# 		double_click(u"Name||Edit")

# mouse.click(button='left', coords=(1477, 770))
# time.sleep(10)
# mouse.click(button='left', coords=(1393, 923))
# mouse.click(button='left', coords=(285, 41))
# mouse.click(button='left', coords=(340, 93))
# mouse.click(button='left',coords=(966, 287))
# mouse_wheel(steps=-10)
# # mouse.click(button='left', coords=(1366, 1000))
# mouse.double_click(button='left', coords=(919, 722))
# audio = os.path.join(directory, "Be Sure To Look At The High Fly's!.wav")
# if os.path.isfile(audio):
# 	name_audio = audio
# 	print(name_audio)
# 	dur = librosa.get_duration(filename=name_audio)
# 	print(dur, " Frames: ", dur*30*2)
# 	send_keys(str(round(dur*30*2)))
# mouse.click(button='left',coords=(1004, 867))
# mouse.click(button='left',coords=(71, 218))
# mouse.click(button='left',coords=(303, 194))
# send_keys('v')
# send_keys('{ENTER}')
# mouse.double_click(button='left',coords=(351, 425))
# send_keys('test')
# mouse.click(button='left',coords=(495, 501))
# time.sleep(20)
# mouse.click(button='left',coords=(988, 567)) #close reminder
# mouse.click(button='left',coords=(1190, 155))
# mouse.click(button='left', coords=(1034, 533))

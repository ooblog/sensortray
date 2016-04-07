#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
#from LTsv_printf import *
from LTsv_file   import *
#from LTsv_time   import *
#from LTsv_calc   import *
#from LTsv_joy    import *
#from LTsv_kbd    import *
from LTsv_gui    import *

sensor_windowW,sensor_windowH=320,240
sensor_ltsvname,sensor_ltsvtext,sensor_config="sensortray.tsv","",""
sensor_Celsius,sensor_blinkC,sensor_blinkT,sensor_wait=0,80,1000,3000
sensor_fontname="kantray5x5comic,12"
sensor_iconname="sensorC.png"
sensor_sensor,sensor_tempO,sensor_tempC="sensors","Core0 Temp:   +","°C"
sensor_iconnameBF,sensor_iconnameAF="",""
sensor_iconblink=False

def sensortray_timeC(callback_void=None,callback_ptr=None):
    global sensor_Celsius
    if sys.platform.startswith("linux"):
        LTsv_sensors=LTsv_subprocess(sensor_sensor)
        LTsv_posL=LTsv_sensors.find(sensor_tempO); LTsv_posR=LTsv_sensors.find(sensor_tempC,LTsv_posL)
        sensor_Celsius=LTsv_intstr0x(LTsv_sensors[LTsv_posL+len(sensor_tempO):LTsv_posR])
    if sys.platform.startswith("win"):
#        LTsv_sensors=LTsv_subprocess("?")
        sensor_Celsius=0
    sensor_Celsius=min(max(sensor_Celsius,0),99)
    LTsv_window_after(sensor_window,event_b=sensortray_timeC,event_i="sensortray_timeC",event_w=sensor_wait)

def sensortray_blinkT(callback_void=None,callback_ptr=None):
    global sensor_Celsius,sensor_notifyicon,sensor_iconnameBF,sensor_iconnameAF,sensor_iconblink
    sensor_iconnameAF="{0}[{1}]".format(sensor_iconname,sensor_Celsius)
    if sensor_Celsius >= sensor_blinkC:
        sensor_iconblink=False if sensor_iconblink else True
        sensor_iconnameAF=LTsv_default_iconuri if sensor_iconblink else sensor_iconnameAF
    if sensor_iconnameBF != sensor_iconnameAF:
        sensor_iconnameBF=sensor_iconnameAF
        LTsv_widget_seturi(sensor_notifyicon,widget_u=sensor_iconnameBF)
        LTsv_widget_settext(sensor_notifyicon,widget_t="{0}[{1}]".format(sensor_iconname,sensor_Celsius))
    LTsv_window_after(sensor_window,event_b=sensortray_blinkT,event_i="sensortray_blinkT",event_w=sensor_blinkT)

def sensor_blinkC_slide(window_objvoid=None,window_objptr=None):
    global sensor_blinkC
    sensor_blinkC=int(float(LTsv_widget_gettext(sensor_scale_blinkC)))

def sensor_wait_slide(window_objvoid=None,window_objptr=None):
    global sensor_wait
    sensor_wait=int(float(LTsv_widget_gettext(sensor_scale_wait)))

def sensor_blinkT_slide(window_objvoid=None,window_objptr=None):
    global sensor_blinkT
    sensor_blinkT=int(float(LTsv_widget_gettext(sensor_scale_blinkT)))

def sensortray_configload():
    global sensor_ltsvname,sensor_ltsvtext,sensor_config
    global sensor_Celsius,sensor_blinkC,sensor_blinkT,sensor_wait
    global sensor_fontname
    global sensor_iconname
    global sensor_sensor,sensor_tempO,sensor_tempC
    sensor_ltsvtext=LTsv_loadfile(sensor_ltsvname)
    sensor_config=LTsv_getpage(sensor_ltsvtext,"sensortray")
    sensor_blinkC=min(max(int(float(LTsv_readlinerest(sensor_config,"blinkC",sensor_blinkC))),0),100)
    sensor_blinkT=min(max(int(float(LTsv_readlinerest(sensor_config,"blinkT",sensor_blinkT))),100),10000)
    sensor_wait=min(max(int(float(LTsv_readlinerest(sensor_config,"wait",sensor_wait))),1000),10000)
    sensor_fontname=LTsv_readlinerest(sensor_config,"font",sensor_fontname)
    sensor_iconname=LTsv_readlinerest(sensor_config,"tray",sensor_iconname)
#    sensor_sensor=LTsv_readlinerest(sensor_config,"sensor",sensor_sensor)
    sensor_tempO=LTsv_readlinerest(sensor_config,"tempO",sensor_tempO)
    sensor_tempC=LTsv_readlinerest(sensor_config,"tempC",sensor_tempC)

def sensortray_menu():
    yield ("「sensortray」の終了",sensortray_exit_before_cbk)
    yield ("",None)
    yield ("「sensortray」の初期化",sensortray_reset_cbk)

def sensortray_reset(window_objvoid=None,window_objptr=None):
    LTsv_widget_setnumber(sensor_scale_blinkC,80)
    LTsv_widget_setnumber(sensor_scale_blinkT,1000)
    LTsv_widget_setnumber(sensor_scale_wait,3000)
sensortray_reset_cbk=LTsv_CALLBACLTYPE(sensortray_reset)

def sensortray_exit_before(window_objvoid=None,window_objptr=None):
    global sensor_ltsvname,sensor_ltsvtext,sensor_config
    sensor_config=LTsv_pushlinerest(sensor_config,"blinkC",str(sensor_blinkC))
    sensor_config=LTsv_pushlinerest(sensor_config,"blinkT",str(sensor_blinkT))
    sensor_config=LTsv_pushlinerest(sensor_config,"wait",str(sensor_wait))
    sensor_ltsvtext=LTsv_putpage(sensor_ltsvtext,"sensortray",sensor_config)
    LTsv_savefile(sensor_ltsvname,sensor_ltsvtext)
    LTsv_window_exit()
sensortray_exit_before_cbk=LTsv_CALLBACLTYPE(sensortray_exit_before)

LTsv_GUI=LTsv_guiinit(LTsv_GUI_Tkinter)
if len(LTsv_GUI) > 0:
    if LTsv_global_Notify() == LTsv_GUI_GTK2:
       sensor_window=LTsv_window_new(event_b=None,widget_t="sensortray",widget_w=sensor_windowW,widget_h=sensor_windowH)
    if LTsv_global_Notify() == LTsv_GUI_WinAPI:
        sensor_window=LTsv_window_new(event_b=sensortray_exit_before,widget_t="sensortray",widget_w=sensor_windowW,widget_h=sensor_windowH)

    sensortray_configload()
    sensor_label_blinkC=LTsv_label_new(sensor_window,widget_t="Ｎ℃以上でアイコンを点滅",widget_x=0,widget_y=sensor_windowH*0//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6,widget_f=sensor_fontname)
    sensor_scale_blinkC=LTsv_scale_new(sensor_window,event_b=sensor_blinkC_slide,widget_s=0,widget_e=100,widget_a=1,widget_x=0,widget_y=sensor_windowH*1//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6)
    LTsv_widget_setnumber(sensor_scale_blinkC,widget_s=str(sensor_blinkC))
    sensor_label_wait=LTsv_label_new(sensor_window,widget_t="「{0}」取得間隔(ミリ秒)".format(sensor_sensor),widget_x=0,widget_y=sensor_windowH*2//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6,widget_f=sensor_fontname)
    sensor_scale_wait=LTsv_scale_new(sensor_window,event_b=sensor_wait_slide,widget_s=100,widget_e=10000,widget_a=100,widget_x=0,widget_y=sensor_windowH*3//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6)
    LTsv_widget_setnumber(sensor_scale_wait,widget_s=str(sensor_wait))
    sensor_label_blinkT=LTsv_label_new(sensor_window,widget_t="アイコン点滅の間隔(ミリ秒)",widget_x=0,widget_y=sensor_windowH*4//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6,widget_f=sensor_fontname)
    sensor_scale_blinkT=LTsv_scale_new(sensor_window,event_b=sensor_blinkT_slide,widget_s=100,widget_e=5000,widget_a=100,widget_x=0,widget_y=sensor_windowH*5//6,widget_w=sensor_windowW,widget_h=sensor_windowH//6)
    LTsv_widget_setnumber(sensor_scale_blinkT,widget_s=str(sensor_blinkT))

    if LTsv_global_Notify() == LTsv_GUI_GTK2:
        sensor_iconname="sensorC.png"; LTsv_default_iconuri="/usr/share/pixmaps/python.xpm"
        LTsv_draw_picture_load(sensor_iconname); LTsv_draw_picture_celldiv(sensor_iconname,10,10)
    if LTsv_global_Notify() == LTsv_GUI_WinAPI:
        sensor_iconname="sensorC.icl"; LTsv_default_iconuri=sys.executable
        LTsv_icon_load(sensor_iconname)
    sensor_notifyicon=LTsv_notifyicon_new(sensor_window,widget_t=sensor_iconname,widget_u="{0}[{1}]".format(sensor_iconname,sensor_Celsius),menu_b=sensortray_menu(),menu_c=sensortray_reset)

    sensortray_timeC()
    sensortray_blinkT()
    if LTsv_global_Notify() == LTsv_GUI_WinAPI:
        LTsv_widget_showhide(sensor_window,True)
    LTsv_window_main(sensor_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

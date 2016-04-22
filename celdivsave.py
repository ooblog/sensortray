#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
import subprocess
os.chdir(sys.path[0])
sys.path.append("LTsv")
#from LTsv_printf import *
#from LTsv_file   import *
#from LTsv_time   import *
#from LTsv_calc   import *
#from LTsv_joy    import *
#from LTsv_kbd    import *
from LTsv_gui    import *

sensor_workdir="./celldivsave/"

LTsv_GUI=LTsv_guiinit(LTsv_GUI_Tkinter)
if len(LTsv_GUI) > 0:
    celldivfile="sensorC.png"; LTsv_draw_picture_load(celldivfile)
    sensor_pictureW,sensor_pictureH=LTsv_global_pictureW(celldivfile),LTsv_global_pictureH(celldivfile)
    sensor_windowW,sensor_windowH=sensor_pictureW*2,sensor_pictureH*2
    sensor_window=LTsv_window_new(event_b=LTsv_window_exit,widget_t="celldivsave",widget_w=sensor_windowW,widget_h=sensor_windowH)
    sensor_canvas=LTsv_canvas_new(sensor_window,widget_x=0,widget_y=0,widget_w=sensor_windowW,widget_h=sensor_windowH)
    LTsv_drawGTK_selcanvas(sensor_canvas)
    LTsv_drawGTK_color("white")
    LTsv_drawGTK_polygonfill(0,0,sensor_windowW,0,sensor_windowW,sensor_windowH,0,sensor_windowH)
    if LTsv_GUI == LTsv_GUI_GTK2:
        if not os.path.isdir(sensor_workdir): os.mkdir(sensor_workdir)
        LTsv_draw_picture_celldiv(celldivfile,10,10)
        sensor_iconsize=sensor_pictureW//10
        for div_x in range(10*10):
           celldivoldfile,celldivnewfile="{0}[{1}]".format(celldivfile,div_x),sensor_workdir+"sensorC[{0:0>2}].png".format(div_x)
           LTsv_drawGTK_picture(celldivoldfile,draw_x=sensor_iconsize//2+sensor_iconsize*2*(div_x%10),draw_y=sensor_iconsize//2+sensor_iconsize*2*(div_x//10))
           LTsv_draw_picture_save(celldivoldfile,celldivnewfile)
        LTsv_draw_picture_save(celldivoldfile,celldivnewfile)
    LTsv_draw_queue(sensor_canvas)
    LTsv_widget_showhide(sensor_window,True)
    LTsv_window_main(sensor_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

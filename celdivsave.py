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
celldivfile="sensorC.png"
celldivX,celldivY=10,10
celldivB=2

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    LTsv_draw_picture_load(celldivfile)
    sensor_pictureW,sensor_pictureH=LTsv_global_pictureW(celldivfile),LTsv_global_pictureH(celldivfile)
    sensor_windowW,sensor_windowH=celldivB+sensor_pictureW+celldivX*celldivB,celldivB+sensor_pictureH+celldivY*celldivB
    sensor_window=LTsv_window_new(event_b=LTsv_window_exit,widget_t="celldivsave",widget_w=sensor_windowW,widget_h=sensor_windowH)
    sensor_canvas=LTsv_canvas_new(sensor_window,widget_x=0,widget_y=0,widget_w=sensor_windowW,widget_h=sensor_windowH)
    LTsv_widget_showhide(sensor_window,True)
    LTsv_draw_selcanvas,LTsv_draw_delete,LTsv_draw_queue,LTsv_draw_picture=LTsv_draw_selcanvas_shell(LTsv_GUI),LTsv_draw_delete_shell(LTsv_GUI),LTsv_draw_queue_shell(LTsv_GUI),LTsv_draw_picture_shell(LTsv_GUI)
    LTsv_draw_color,LTsv_draw_bgcolor,LTsv_draw_font,LTsv_draw_text=LTsv_draw_color_shell(LTsv_GUI),LTsv_draw_bgcolor_shell(LTsv_GUI),LTsv_draw_font_shell(LTsv_GUI),LTsv_draw_text_shell(LTsv_GUI)
    LTsv_draw_polygon,LTsv_draw_polygonfill=LTsv_draw_polygon_shell(LTsv_GUI),LTsv_draw_polygonfill_shell(LTsv_GUI)
    LTsv_draw_squares,LTsv_draw_squaresfill=LTsv_draw_squares_shell(LTsv_GUI),LTsv_draw_squaresfill_shell(LTsv_GUI)
    LTsv_draw_circles,LTsv_draw_circlesfill=LTsv_draw_circles_shell(LTsv_GUI),LTsv_draw_circlesfill_shell(LTsv_GUI)
    LTsv_draw_points=LTsv_draw_points_shell(LTsv_GUI)
    LTsv_draw_arc,LTsv_draw_arcfill=LTsv_draw_arc_shell(LTsv_GUI),LTsv_draw_arcfill_shell(LTsv_GUI)
    LTsv_drawGTK_selcanvas(sensor_canvas)
    LTsv_drawGTK_color("#FBFBFB")
    LTsv_drawGTK_polygonfill(0,0,sensor_windowW,0,sensor_windowW,sensor_windowH,0,sensor_windowH)
    if LTsv_GUI == LTsv_GUI_GTK2:
        if not os.path.isdir(sensor_workdir): os.mkdir(sensor_workdir)
        LTsv_draw_picture_celldiv(celldivfile,celldivX,celldivY)
        for div_xy in range(celldivX*celldivY):
           celldivoldfile,celldivnewfile="{0}[{1}]".format(celldivfile,div_xy),sensor_workdir+"sensorC[{0:0>2}].png".format(div_xy)
           cellx,celly=(sensor_pictureW//celldivX)*(div_xy%celldivY),(sensor_pictureH//celldivY)*(div_xy//celldivY)
           LTsv_draw_picture(celldivoldfile,celldivB+(sensor_pictureW//celldivX+celldivB)*(div_xy%celldivX),celldivB+celldivB+(sensor_pictureH//celldivY+celldivB)*(div_xy//celldivX))
           LTsv_draw_picture_save(celldivoldfile,celldivnewfile)
    LTsv_drawGTK_queue()
    LTsv_window_main(sensor_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

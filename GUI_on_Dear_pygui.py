# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 22:26:37 2022

@author: erofe
"""
import dearpygui.dearpygui as dpg

dpg.create_context()

def resize_img():
    print(dpg.get_item_rect_size("Window"))
    height, width = dpg.get_item_rect_size("Window")
    size = height
    dpg.set_item_height("drawlist", size)
    dpg.set_item_width("drawlist", size)
    if dpg.does_alias_exist:
        dpg.delete_item("drawlist", children_only=True)
    dpg.draw_image("image_id", (0, 0), (size, size), uv_min=(0, 0), uv_max=(1, 1), parent="drawlist")


width, height, channels, data = dpg.load_image('Somefile.jpg')
with dpg.texture_registry():
    dpg.add_static_texture(width, height, data, tag="image_id")

with dpg.item_handler_registry(tag="window_handler"):
    dpg.add_item_resize_handler(callback=resize_img)

with dpg.window(tag="Window"):
    with dpg.drawlist(tag="drawlist", width=200, height=200, parent="Window"):
        height, width = dpg.get_item_rect_size("Window")
        print(dpg.get_item_rect_size("drawlist"))
        print(height)
        dpg.draw_image("image_id", (0, 0), (height, width), uv_min=(0, 0), uv_max=(1, 1))

dpg.bind_item_handler_registry("Window", "window_handler")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
"""

import dearpygui.dearpygui as dpg

dpg.create_context()

width, height, channels, data = dpg.load_image("Somefile.jpg")

with dpg.texture_registry(show=True):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

with dpg.window(label="Tutorial",tag="Primary Window"):
    dpg.add_image("texture_tag")


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
"""
"""
Шаблон программы 
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window",tag="Primary Window"):
    dpg.add_text("Hello, world")

dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

"""
# encoding=utf8

from PIL import Image
from io import BytesIO

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import tkinter
from tkinter import Button
tkWindow = tkinter.Tk()

tkWindow.geometry("800x600+200+200")
tkWindow.title("Time Tracker")

# import subprocess
# subprocess.call("C:\Google analytics.docx")

import os
import mouse
import win32gui, win32con, win32process

# import keyboard
import pyautogui
# from docx import Document
# from docx.shared import Inches
# import win32gui
# from PIL import ImageGrab
#
# shotfile = "C:\\Users\\Korisnik\\Desktop\\Screenshot 2023-04-12 105201.png"  # temporary image storage
# docxfile = "C:\\Users\\Korisnik\\Desktop\\Google analytics.docx" # main document
# hotkey = 'ctrl+shift+q'  # use this combination anytime while script is running
#
# def do_cap():
#     try:
#         print ('Storing capture...')
#
#         hwnd = win32gui.GetForegroundWindow()  # active window
#         bbox = win32gui.GetWindowRect(hwnd)  # bounding rectangle
#
#         # capture screen
#         shot = pyautogui.screenshot(region=bbox) # take screenshot, active app
#         # shot = pyautogui.screenshot() # take screenshot full screen
#         shot.save(shotfile) # save screenshot
#
#         # append to document. Doc must exist.
#         doc = Document(docxfile) # open document
#         doc.add_picture(shotfile, width=Inches(7))  # add image, 7 inches wide
#         doc.save(docxfile)  # update document
#         print ('Done capture.')
#     except Exception as e:  # allow program to keep running
#         print("Capture Error:", e)


def open():
    options = Options()

    os.startfile("C:\\Users\\Korisnik\\Desktop\\test.txt")
    time.sleep(2)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    time.sleep(2)
    mouse.wheel(-14)

#     options.headless = True
#
#     driver = webdriver.Chrome(chrome_options=options)
#
#     driver.maximize_window()
#     driver.get("https://en.wikipedia.org/wiki/Main_Page")
#     tkWindow.after(500, save_screenshot(os))

# def save_screenshot(driver):
#     total_width = driver.execute_script("return document.body.offsetWidth")
#     total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
#     viewport_width = driver.execute_script("return document.body.clientWidth")
#     viewport_height = driver.execute_script("return window.innerHeight")
#
#     myHeight = 0
#     i = 1
#
#     while myHeight < total_height:
#         driver.execute_script("window.scrollTo({0}, {1})".format(total_width, myHeight - 50))
# #         time.after(0.5)
#
#         driver.set_window_size(viewport_width, viewport_height)
#         img_binary = driver.get_screenshot_as_png()
#         img = Image.open(BytesIO(img_binary))
#         img.save("screen"+str(i)+".png")
#         print(" screenshot "+str(i)+" saved")
#
#         myHeight = myHeight + viewport_height
#         i = i + 1

# def after_open():

#     si = win32process.STARTUPINFO()
#     si.dwFlags = win32con.STARTF_USESHOWWINDOW
#     si.wShowWindow = win32con.SW_MAXIMIZE
#     EXE_NAME = r"C:\Windows\notepad.exe"
#     h_proc, h_thr, pid, tid = win32process.CreateProcess(None, EXE_NAME, None, None, False, 0, None, None, si)

but = Button(tkWindow, text = "Load Table", command = open)
but.pack(side="top", anchor = "w", padx=15, pady=35)

tkWindow.mainloop()
import sys
import os
import threading
import time
import subprocess
import pyautogui
import win32gui, win32con
import pytesseract
from PIL import Image
import datetime

import create_database
import show_databases

import tkinter
from tkinter import *
from tkinter import Button
tkWindow = tkinter.Tk()

tkWindow.title("Scanner")
width= tkWindow.winfo_screenwidth()
height= tkWindow.winfo_screenheight()
tkWindow.geometry("%dx%d" % (width, height))

databases = show_databases.show_databases()
variable = StringVar()
variable.set(databases[2])
drop = OptionMenu( tkWindow, variable , *databases )
drop.pack()

def scan_app():
    # Change the path of the text file to your own file path
    program_path = "C:/Users/Korisnik/Desktop/hello/test/test.bat"

    # Change the path of the output folder to your own folder path
    output_folder = "C:/Users/Korisnik/Desktop/hello/images"

    # Set the delay between each scroll (in seconds)
    scroll_delay = 1

    # Set the size of the screenshot
    screenshot_size = (1920, 1080)

    # Open the program
    process = subprocess.Popen(program_path)

    # Wait for the program to start up
    time.sleep(2)

    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    # Get the initial position of the mouse cursor
    start_position = pyautogui.position()
    print("start_position",start_position)

    # Wait for the program to start up
    time.sleep(3)

    # Log
    textbox.config(state=tkinter.NORMAL)
    textbox.insert('end',"Start scanning the program \n")
    textbox.config(state=tkinter.DISABLED)

    # Scroll through the program, taking a screenshot at each scroll
    i = 0
    while i<2:

        # Take a screenshot of the current section
        screenshot = pyautogui.screenshot(region=(0, 0, *screenshot_size))

        # Save the screenshot to the output folder
        screenshot.save(os.path.join(output_folder, f"scroll_{i}.png"))

        time.sleep(2)

        pyautogui.scroll(-1700)

        # Wait for the program to finish scrolling
        time.sleep(3)

        # Log
        textbox.config(state=tkinter.NORMAL)
        textbox.insert('end', f"Screenshot {i} taken \n" )
        textbox.config(state=tkinter.DISABLED)

        i += 1


    # Log
    textbox.config(state=tkinter.NORMAL)
    textbox.insert('end',"Scanning finished \n")
    textbox.config(state=tkinter.DISABLED)

    win32gui.PostMessage(hwnd,win32con.WM_CLOSE,0,0)


but = Button(tkWindow, text = "Read", command = threading.Thread(target=scan_app).start)
but.pack(side="top", anchor = "w", padx=15, pady=15)


def write_img():
    # Set the path of the folder containing the images
    input_folder = "C:/Users/Korisnik/Desktop/hello/images"

    # Set the path of the output file
    new_database_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    output_file = "C:/Users/Korisnik/Desktop/hello/databases/"+new_database_name+".sql"

    # Initialize pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Korisnik\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Iterate through each image in the folder
        for i, image_file in enumerate(os.listdir(input_folder)):
            # Load the image
            image_path = os.path.join(input_folder, image_file)
            image = Image.open(image_path)

            # Perform OCR on the image
            text = pytesseract.image_to_string(image)

            # Write the recognized text to the output file
            f.write(text)
            f.write("\n\n")

            # Log
            textbox.config(state=tkinter.NORMAL)
            textbox.insert('end', "Image " + image_path + " data stored in file \n")
            textbox.config(state=tkinter.DISABLED)

    # Log
    textbox.config(state=tkinter.NORMAL)
    textbox.insert('end',"File ready \n")
    textbox.config(state=tkinter.DISABLED)

    create_database.create_database(new_database_name)

but1 = Button(tkWindow, text = "Write", command = threading.Thread(target=write_img).start)
but1.pack(side="top", anchor = "w", padx=15, pady=0)

textbox = tkinter.Text(tkWindow,state=tkinter.DISABLED, width = width, height = 10)
textbox.pack(anchor = "w",side=tkinter.BOTTOM)
tkWindow.mainloop()
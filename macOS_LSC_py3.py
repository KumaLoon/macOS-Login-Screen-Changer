#Copyright (c) 2015 - 2017 Seon Jun Choi
from tkinter import filedialog
from tkinter import *
import shutil
import os
import sys
os.system ('read -p "By continuing, you are agreeing to the terms of the software license agreement and you acknowlege all the information that was provided in license file (Press enter to continue)"')
os.system("clear")
if os.path.isfile(os.path.expanduser("~/Documents/OSX_LS/com.apple.desktop.admin.png.backup")) == True:
    print("You have used this tool before, welcome back!\n")
    print("1. Install a new lockscreen")
    print("2. Restore to original lockscreen\n")
    print("Q. Quit")
    ans = input("Choice: ")
    if ans == "1":
        back = input("Do you want to keep original lockscreen file? If yes, it will not back up the current lockscreen. (y/n): ")
        if back == "y" or back == "Y":
            os.system("mv /Library/Caches/com.apple.desktop.admin.png ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup")
        print("Please select your image")
        image = Tk()
        image.filename =  filedialog.askopenfilename(initialdir = "~/",title = ".",filetypes = (("PNG","*.png"),("JPEG","*.jpg")))
        shutil.copy2(image.filename, "/Library/Caches/com.apple.desktop.admin.png")
        print("done")
        sys.exit(0)
    elif ans == "2":
        os.system("mv ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup /Library/Caches/com.apple.desktop.admin.png")
        os.system("rm -rf ~/Documents/OSX_LS")
        print("done")
        sys.exit(0)
    else:
        sys.exit(0)
else:
    print("Hello! Welcome to OS X Login Screen Changer!")
    print("Your lockscreen back up will be saved in ~/Documents/OSX_LS\n")
    print("1. Install a new lockscreen\n")
    print("Q. Quit")
    ans = input("Choice: ")
    if ans == "1":
        os.system("mkdir ~/Documents/OSX_LS")
        os.system("mv /Library/Caches/com.apple.desktop.admin.png ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup")
        print("Please select your image")
        image = Tk()
        image.filename =  filedialog.askopenfilename(initialdir = "~/",title = ".",filetypes = (("PNG","*.png"),("JPEG","*.jpg")))
        shutil.copy2(image.filename, "/Library/Caches/com.apple.desktop.admin.png")
        print("done")
        sys.exit(0)
    else:
        sys.exit(0)

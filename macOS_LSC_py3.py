from tkinter import FileDialog
form shutil
import os
def findfile():
  if os.path.isfile(~/Documents/OSX_LS/com.apple.desktop.admin.png.backup) == True:
    print("You have used this tool before, welcome back!\n")
    print("1. Install a new lockscreen")
    print("2. Restore to original lockscreen\n")
    print("Q. Quit")
    ans = input("Choice: ")
    if ans == 1:
      back = input("Do you want to keep original lockscreen file? If yes, it will not back up the current lockscreen. (y/n): ")
      if back == "y" or back == "Y":
        os.system("mv /Library/Caches/com.apple.desktop.admin.png ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup")
      image = Tk()
      image.filename =  filedialog.askopenfilename(initialdir = "~/",title = "Please select your image(png and jpeg only)",filetypes = (("PNG","*.png"),("JPEG","*.jpg")))
      shutil.copy2(image.filename, "/Library/Caches/com.apple.desktop.admin.png")
      print("done")
      sys.exit(0)
    elif ans == 2:
      os.system("mv ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup /Library/Caches/com.apple.desktop.admin.png")
      os.system("rm -rf ~/Documents/OSX_LS)
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
      if ans == 1:
        os.system(mkdir ~/Documents/OSX_LS)
        image = Tk()
        image.filename =  filedialog.askopenfilename(initialdir = "~/",title = "Please select your image(png and jpeg only)",filetypes = (("PNG","*.png"),("JPEG","*.jpg")))
        shutil.copy2(image.filename, "/Library/Caches/com.apple.desktop.admin.png")
      sys.exit(0)        
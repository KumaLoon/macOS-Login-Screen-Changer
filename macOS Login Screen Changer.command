#!/bin/bash

clear

# LICENSE AGREEMENT
read -p "By continuing, you are agreeing to the terms of the software license agreement and you acknowlege all the information that was provided in license file (Press enter to continue)"

# Checking backup location
clear
if [ -f ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup ]; then
    echo "You have used this tool before, welcome back!"
    Menu (){
    echo "Your lockscreen back up is saved in ~/Documents/OSX_LS"
    echo ""
    echo "1. Install a new lockscreen"
    echo "2. Restore to original lockscreen"
    echo ""
    echo "Q. Quit"

    read ANSWER

    case "$ANSWER" in

    1)
    while [[ -z "$BKUPOSX" ]]
    do
    clear
    read -p "Do you want to keep original lockscreen file? If yes, it will not back up the current lockscreen. (y/n): " BKUPOSX
    done
    if [ "$BKUPOSX" == "Y" ] && [ "$BKUPOSX" == "y" ]; then
        osascript -e 'display dialog "Please select the image you want to use" buttons "OK"'
        LOCATION="$(osascript -e 'tell application "Terminal" to return POSIX path of (choose file)')"
        wait
        cd /Library/Caches
        cp $LOCATION /Library/Caches/com.apple.desktop.admin.png
        echo "Done"
        exit 0
    elif [ "$BKUPOSX" == "N" ] && [ "$BKUPOSX" == "n" ]; then
        osascript -e 'display dialog "Please select the image you want to use" buttons "OK"'
        LOCATION="$(osascript -e 'tell application "Terminal" to return POSIX path of (choose file)')"
        wait
        cd /Library/Caches
        mv com.apple.desktop.admin.png ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup
        cp $LOCATION /Library/Caches/com.apple.desktop.admin.png
        echo "Done"
        exit 0
    fi
    ;;

    2)
    cd ~/Documents/OSX_LS
    mv com.apple.desktop.admin.png.backup /Library/Caches/com.apple.desktop.admin.png
    echo "Done"
    exit 0
    ;;

    Qq)
    exit 0
    ;;

    esac
    exit
    }
    Menu

else

    echo "Hello! Welcome to OS X Login Screen Changer!"
    echo "Your lockscreen back up will be saved in ~/Documents/OSX_LS"

    Menu1 () {
    echo ""
    echo "1. Install a new lockscreen"
    echo ""
    echo "Q. Quit"

    read ANSWER

    case "$ANSWER" in

    1)
    cd ~/Documents
    if [ -d ~/Documents/OSX_LS ]; then
        :
    else
        mkdir OSX_LS
    fi
    osascript -e 'display dialog "Please select the image you want to use" buttons "OK"'
    LOCATION="$(osascript -e 'tell application "Terminal" to return POSIX path of (choose file)')"
    wait
    cd /Library/Caches
    mv com.apple.desktop.admin.png ~/Documents/OSX_LS/com.apple.desktop.admin.png.backup
    cp $LOCATION /Library/Caches/com.apple.desktop.admin.png
    echo "Done"
    exit 0
    ;;

    Qq)
    exit 0
    ;;

    esac
    }
    Menu1

fi
exit 0

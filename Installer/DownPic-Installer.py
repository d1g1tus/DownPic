import os
import ssl
import urllib.request

import winshell
import git
from win32com.client import Dispatch

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.github.com/d1g1tus/DownPic'

dirs = 'C:/Program Files/DownPic/'


class MESSAGES:

    @staticmethod
    def print_main():
        os.system("cls")
        print('''
            //////////////////////////////////////////////////////////////////////
            ///////////////////// CHOOSE AN OPTION ///////////////////////////////
            //////////////////////////////////////////////////////////////////////
            ////// 1 -> Install DownPic Alpha 1.0 ////////////////////////////////
            ////// 2 -> Create a Desktop Shortcut for Downpic ////////////////////
            ////// 3 -> Visit my GitHub //////////////////////////////////////////
            ////// 4 -> Uninstall Everything /////////////////////////////////////
            ////// 5 -> Exit /////////////////////////////////////////////////////
            //////////////////////////////////////////////////////////////////////
            //////////////////////////////////////////////////////////////////////''')

    @staticmethod
    def downloading_downpic():
        os.system("cls")
        print('''
        \n---------------------------------------------------------------------------------------------
        //////////////////////////////// DOWNPIC DOWNLOAD - UPDATE //////////////////////////////////
        ---------------------------------------------------------------------------------------------
        /////////////////////////////////////////////////////////////////////////////////////////////
        /////////////////////////////////////////////////////////////////////////////////////////////
        ///// Please, take into account that this function will download DownPic directly from //////
        ///// its GitHub repository, so this will also work as an updater. So use this function /////
        ///// to install DownPic and/or Update DownPic. /////////////////////////////////////////////
        /////////////////////////////////////////////////////////////////////////////////////////////
        /////////////////////////////////////////////////////////////////////////////////////////////\n
        ''')
        os.system("pause")

    @staticmethod
    def print_python_download():
        os.system("cls")
        print('''
        \n////////////////////////////////////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////////////////////////////////////
        ///// So it looks like you don't have Python installed. What a pity... /////////////////////////
        ///// The problem here is that we need Python in your system to run DownPic... /////////////////
        ///// So if you don't mind we're going to install it on your system too ////////////////////////
        ///// For this part of the installation I will need you to press a bunch of buttons ////////////
        ///// Don't worry, the rest is up to me. Ok? I will run a Windows Installer ////////////////////
        ///// It's Python's Official App for Windows. Install that sucker, and then come back here /////
        ///// I'll be waiting. When it finishes, press any button here to continue with ////////////////
        ///// DownPic installation /////////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////////////////////////////////////\n
        ''')
        os.system("pause")


class DOWNLOAD:

    @staticmethod
    def install_pip():
        os.system("cls")
        print("\n ///// -> Upgrading pip version\n")
        os.system("Python -m pip install --upgrade pip")
        print("///// -> Pip Version successfully upgraded!\n")
        print("///// -> Installing the required packages. This might take a while...\n")
        print("///// -> Installing easygui\n")
        os.system("pip install easygui")
        print("///// -> Easygui successfully installed!\n")
        print("///// -> Installing pynput\n")
        os.system("pip install pynput")
        print("///// -> pynput successfully installed!\n")
        print("///// -> Installing requests\n")
        os.system("pip install requests")
        print("///// -> requests successfully installed!\n")
        print("///// -> Installing pyperclip\n")
        os.system("pip install pyperclip")
        print("///// -> pyperclip successfully installed!\n")
        print("///// -> Installing Image\n")
        os.system("pip install Image")
        print("///// -> Image successfully installed!\n")
        print("\n ///// -> All packages were successfully installed!\n")
        os.system("pause")

    @staticmethod
    def start_python_download():
        MESSAGES.print_python_download()
        python = "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe"
        print("\n///// -> Starting download \n")
        urllib.request.urlretrieve(python, "C:/Users/Public/python.exe")
        print("///// -> Python successfully downloaded! Running Python installation\n")
        os.system("start C:/Users/Public/python.exe")
        os.system("pause")

    @staticmethod
    def download_python():
        python = os.system("where Python")
        if python == 0:
            os.system("cls")
            print("\n//////// -> PYTHON is already installed!\n")
            os.system("pause")
            DOWNLOAD.install_pip()

        if python == 1:
            DOWNLOAD.start_python_download()
            DOWNLOAD.install_pip()

    @staticmethod
    def create_desktop_exe():
        desktop = winshell.desktop()
        path = os.path.join(desktop, "DOWNPIC.lnk")
        target = r"C:/Program Files/DownPic/bin/Launcher.bat"
        wDir = r"C:/Program Files/DownPic/"
        icon = r"C:/Program Files/DownPic/bin/Data/Installation/Icons/Icon1.ico"
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.WindowStyle = 7
        shortcut.save()

while True:
    try:
        MESSAGES.print_main()
        opt = int(input("    ////////// -> "))
    
        if opt == 1:
            MESSAGES.downloading_downpic()
            git.Repo.clone_from(url, dirs)
            print("\n ///// -> DownPic has been successfully downloaded!!!\n")
            os.system("pause")
            DOWNLOAD.download_python()
            print("///// -> Python was successfully installated! \n")
            os.system("pause")
            os.system("cls")
        if opt == 2:
            DOWNLOAD.create_desktop_exe()
            print("\n ///// -> Shortcut has been successfully created!!!!\n")
            os.system("pause")
            os.system("cls")
        if opt == 3:
            os.system("start https://github.com/d1g1tus/DownPic")
            os.system("cls")
        if opt == 4:
            while True:
                try:
                    opl = input("\nAre you sure you want to uninstall DownPic? y/n -> ")
                    if opl == "y":
                        os.remove("C:/Program Files/DownPic")
                        print("\n ////// DownPic has been successfully uninstalled!!")
                        break
                    if opl == "n":
                        break
                except TypeError:
                    pass
    
            os.system("pause")
            os.system("cls")
        if opt == 5:
            break
        else:
            os.system("cls")
    
    except TypeError:
        pass

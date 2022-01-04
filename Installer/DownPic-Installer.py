import urllib
import os
import ssl
from urllib import request
ssl._create_default_https_context = ssl._create_unverified_context

# DIR VARS
downpic_path = "C:/Program Files/DownPic/"
bin_path = "C:/Program Files/DownPic/bin/"
core_path = "C:/Program Files/DownPic/bin/Core/"
data_path = "C:/Program Files/DownPic/bin/Data/"
img_path = "C:/Program Files/DownPic/bin/Data/Images/"
var_path = "C:/Program Files/DownPic/bin/Data/variables/"
func_path = "C:/Program Files/DownPic/bin/functions/"
guis_path = "C:/Program Files/DownPic/bin/guis/"

dir_vars = [downpic_path, bin_path, core_path, data_path, img_path, var_path, func_path, guis_path]

init_url = 'https://cdn-147.anonfiles.com/N7s6Z543xb/35e1f5cc-1641278769/__init__.py'
# "C:/Program Files/DownPic/"
launcher_url = 'https://cdn-108.anonfiles.com/F4r9Z549x6/f75963ab-1641278562/Launcher%20-%20DownPic.py'
downpicexe_url = 'https://cdn-147.anonfiles.com/J6jeZ94bxa/9b9890f3-1641277222/DownPic.exe'
# "C:/Program Files/DownPic/bin/Core/" + init
config_url = 'https://cdn-147.anonfiles.com/D8pbZ941xb/c5f12134-1641278266/config.py'
downpic_url = 'https://cdn-148.anonfiles.com/X7p6Za4ax3/c47ccaac-1641278334/DownPic.py'
# "C:/Program Files/DownPic/bin/Data/Images/"
img_url = 'https://cdn-147.anonfiles.com/f3qdZ64dx2/971fe99d-1641278364/background_main.png'
# "C:/Program Files/DownPic/bin/Data/variables/" + init
default_variables_url = 'https://cdn-101.anonfiles.com/Z5qbZ346xb/b670e8c3-1641278403/default_variables.py'
variables_url = 'https://cdn-133.anonfiles.com/ncreZ24ax8/c98b5b62-1641278444/variables.py'
# "C:/Program Files/DownPic/bin/functions/" + init
config_main_functions_url = 'https://cdn-103.anonfiles.com/r7raZ845xc/ff40d11e-1641278463/config_main_functions.py'
main_functions_url = 'https://cdn-125.anonfiles.com/z0r5Z641x1/bdfc1ce8-1641278487/main_functions.py'
# "C:/Program Files/DownPic/bin/guis/" + init
messages_url = 'https://cdn-104.anonfiles.com/5cr0Z044x0/6ae9708b-1641278514/messages.py'


class DOWNLOAD:

    @staticmethod
    def info_make_dir(info):
        return print("Creating folder -> " + info)

    @staticmethod
    def make_dir():
        print("\n-----------------------------------------------------------")
        print("/////////// STARTING CREATING FOLDERS - COFFEE BREAK")
        print("-----------------------------------------------------------\n")

        for i in range(len(dir_vars)):
            os.mkdir(dir_vars[i])
            DOWNLOAD.info_make_dir(dir_vars[i])

        print("-----------------------------------------------------------")
        print("////////// ALL FOLDERS HAVE BEEN CREATED SUCCESSFULLY!!!")
        print("-----------------------------------------------------------\n")

    @staticmethod
    def download_files():
        print("-----------------------------------------------------------")
        print("////////STARTING FILES DOWNLOAD - THIS MIGHT TAKE A WHILE")
        print("-----------------------------------------------------------\n")
        urllib.request.urlretrieve(launcher_url, downpic_path + "Launcher - DownPic.py")
        print("Downloaded -> Launcher - DownPic.py in: " + downpic_path)
        urllib.request.urlretrieve(downpicexe_url, downpic_path + "DownPic.exe")
        print("Downloaded -> DownPic.exe in: " + downpic_path)
        urllib.request.urlretrieve(init_url, core_path + "__init__.py")
        print("Downloaded -> __init__.py in: " + core_path)
        urllib.request.urlretrieve(config_url, core_path + "config.py")
        print("Downloaded -> config.py in: " + core_path)
        urllib.request.urlretrieve(downpic_url, core_path + "DownPic.py")
        print("Downloaded -> DownPic.py in: " + core_path)
        urllib.request.urlretrieve(img_url, img_path + "background_main.png")
        print("Downloaded -> background.png in: " + img_path)
        urllib.request.urlretrieve(init_url, var_path + "__init__.py")
        print("Downloaded -> __init__.py in: " + var_path)
        urllib.request.urlretrieve(default_variables_url, var_path + "default_variables.py")
        print("Downloaded -> default_variables.py in: " + var_path)
        urllib.request.urlretrieve(variables_url, var_path + "variables.py")
        print("Downloaded -> variables.py in: " + var_path)
        urllib.request.urlretrieve(init_url, func_path + "__init__.py")
        print("Downloaded -> __init__.py in: " + func_path)
        urllib.request.urlretrieve(config_main_functions_url, func_path + "config_main_functions.py")
        print("Downloaded -> config_main_functions.py in: " + func_path)
        urllib.request.urlretrieve(main_functions_url, func_path + "main_functions.py")
        print("Downloaded -> main_functions.py in: " + func_path)
        urllib.request.urlretrieve(init_url, guis_path + "__init__.py")
        print("Downloaded -> __init__.py in: " + core_path)
        urllib.request.urlretrieve(messages_url, guis_path + "messages.py")
        print("Downloaded -> messages.py in: " + func_path + '\n')
        print("-----------------------------------------------------------")
        print("///////// ALL DOWNLOADS WERE COMPLETED SUCCESSFULLY!!!")
        print("-----------------------------------------------------------\n")

    @staticmethod
    def create_desktop_exe():
        userprofile = os.environ.get('USERPROFILE')
        desktop = userprofile + '/Desktop/DownPic.exe'
        urllib.request.urlretrieve(downpicexe_url, desktop)
        print("\n-----------------------------------------------------------")
        print("///////// SHORTCUT CREATED SUCCESSFULLY!!!")
        print("-----------------------------------------------------------\n")


while True:
    print('''
    //////////////////////////////////////////////////////////////////////
    ///////////////////// CHOOSE AN OPTION ///////////////////////////////
    //////////////////////////////////////////////////////////////////////
    ////// 1 -> Install DownPic Alpha 1.0 ////////////////////////////////
    ////// 2 -> Create a Desktop Shortcut for Downpic ////////////////////
    ////// 3 -> Visit my GitHub //////////////////////////////////////////
    ////// 4 -> Uninstall Everything (Comming Soon)///////////////////////
    ////// 5 -> Exit /////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////////////''')
    opt = int(input("    ////////// -> "))

    if opt == 1:
        DOWNLOAD.make_dir()
        DOWNLOAD.download_files()
        os.system("pause")
        os.system("cls")
    if opt == 2:
        DOWNLOAD.create_desktop_exe()
        os.system("pause")
        os.system("cls")
    if opt == 3:
        os.system("start https://github.com/d1g1tus/DownPic")
        os.system("cls")
    if opt == 4:
        print("\nComming soon. Pinky promise <3\n")
        os.system("pause")
        os.system("cls")
    if opt == 5:
        break
    else:
        os.system("cls")

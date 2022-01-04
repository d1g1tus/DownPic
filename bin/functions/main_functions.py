import os
import shutil
import urllib
import pynput.mouse
import easygui
import time
import pynput.mouse
import ssl
import requests
import pyperclip as clipboard

from urllib import request
from bin.Data.variables import variables as vr
from bin.functions import config_main_functions as cfm
from bin.Data.variables import default_variables as vrd

global far

ssl._create_default_https_context = ssl._create_unverified_context
downloadpath = vr.downloadpath

def folder_exist_check(search_path):
    if os.path.isdir(search_path) is False:
        os.mkdir(search_path)

def file_exist_check(filename, search_path):

    for root, dir, files in os.walk(search_path):
        if filename in files:
            pass
        else:
            file = search_path + filename
            f = open(file, 'w+')
            f.close()

def write_group_header(lista):
    file_exist_check(vr.txt_file_name, vr.logfilespath)
    with open(vr.today_txt_file, 'a') as fr:
        fr.writelines('\n')
        fr.write(' - '.join(lista))
        fr.write(' ')
        fr.write('\n')
        fr.write(vr.line)


def read_txt(path):
    with open(path, 'r') as fars:
        text = fars.readlines()
        return text


def write_links_txt(linkalist):
    with open(vr.today_txt_file, 'a') as writetxt:
        writetxt.write('\n')
        writetxt.writelines('\n'.join(linkalist))
        writetxt.write('\n')


def write_auto_keep(current_file):
    shutil.copy(current_file, vr.pathautokeep)


def write_line_auto_keep(current_file):
    with open(current_file, 'a') as lineadd:
        lineadd.write('\n')
        lineadd.write(vr.line)


def txt_after_download(current_file):

    shutil.copy(vr.pathautokeep, current_file)


def read_autokeep():
    with open(vr.pathautokeep, 'r') as afar:
        keep = afar.readlines()
        return keep


def url_checker(url):
    list1 = []
    list1[:0] = url
    list2 = ['h', 't', 't', 'p']
    j = -1
    asuma = 0
    for i in range(len(list2)):
        j = j + 1
        if list1[i] == list2[j]: 
            asuma = asuma + 1
    if asuma == 4:   
        if vr.firstlink is True:  
            vr.linklist.append(url)
            vr.firstlink = bool(False) 
        else:
            if url in vr.linklist:  
                easygui.msgbox(msg='Link was already in list. Not included...')
                pass
            else:  
                vr.linklist.append(url)

    else:
        pass


def on_click(x, y, button, pressed):
    if vr.mousewhisperer is True:
        if vr.mouseholder is False:
            if button == pynput.mouse.Button.right:
                vr.rmcounter = vr.rmcounter + 1
                if vr.rmcounter == 2:
                    vr.rmcounter = 0
                    vr.mouseholder = bool(True)  

        else:
            if button == pynput.mouse.Button.left:
                vr.rlcounter = vr.rlcounter + 1
                if vr.rlcounter == 2:
                    time.sleep(0.4)
                    link = clipboard.paste()
                    link = str(link)
                    url_checker(link) 
                    vr.rlcounter = 0
                    vr.mouseholder = bool(False) 


def disable_item():
    pass


def download(sendero, name, urls):
    global current_dw_path
    for i in range(len(urls)):
        try:
            fullname = str(name) + vr.name_format + str(i) + vr.file_format 
            fullpathdownload = sendero + '/' + fullname  
            urllib.request.urlretrieve(urls[i], fullpathdownload) 
        except:
            fullname = str(name) + vr.name_format + str(i) + vr.file_format 
            fullpathdownload = sendero + fullname
            r = requests.get(urls[i], stream=True)
            if r.status_code == 200:
                with open(fullpathdownload, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
    urls.clear()
    current_dw_path = vr.downloadpath


def listarurls(position, keep):
    urls = []
    nextline = keep.index(vr.line, position+1)
    distance = keep[position+1:nextline]
    for j in range(len(distance)):
        try:
            list1 = []
            list1[:0] = distance[j]
            list2 = ['h', 't', 't', 'p']
            lol = -1
            asuma = 0
            for k in range(len(list2)):
                lol = lol + 1
                if list2[k] == list1[lol]:
                    asuma = asuma + 1
                if asuma == 4:
                    urls.append(distance[j].strip())
        except IndexError:
            pass
        except ValueError:
            pass

    return urls


def crear_carpetas(header):
    header = header.split(' - ')
    for element in header:
        if element != '':
            vr.rutas.append(element.strip())

    global current_dw_path
    current_dw_path = vr.downloadpath
    for j in range(len(vr.rutas)):
        if not os.path.isdir(current_dw_path + vr.rutas[j]):
            os.mkdir(current_dw_path + vr.rutas[j] + '/')

            current_dw_path = current_dw_path + vr.rutas[j] + '/'
        else:
            current_dw_path = current_dw_path + vr.rutas[j] + '/'

    return current_dw_path


def download_manager_links(current_file):

    with open(current_file, 'r') as f:
        keep = f.readlines()

    for i in range(len(keep)):
        if keep[i] == vr.line:
            grouptitle = keep[i - 1]
            f = crear_carpetas(grouptitle)
            try:
                x = listarurls(i, keep)
                download(f, vr.rutas[1], x)
                vr.rutas.clear()
            except ValueError:
                pass


def declare_download_def_path():

    strin = os.environ.get('USERPROFILE') + "/Downloads/"
    path = 'downloadpath = ' + '"' + cfm.dismantle_unicode_bars(strin) + '"'
    basepath = 'downloadpath = "None"'

    with open(vr.defa_vari_path, 'r') as d:
        defapyfile = d.readlines()
    d.close()

    variables_list = []

    for i in range(len(defapyfile)): 
        variables_list.append(defapyfile[i].strip())

    for j in range(len(variables_list)):
        if variables_list[j] != basepath:
            pass
        else:  # If we find our string
            indice = variables_list.index(variables_list[j])
            # print("tenemos Indice")
            with open(vrd.defa_vari_path, 'w+') as rw:
                defapyfile[indice] = path  
                rw.writelines(defapyfile)
                rw.close()
            break




import os
import easygui
import shutil

from bin.Data.variables import variables as vr
from bin.Data.variables import default_variables as vrd


def sel_nwbg_path():
    file = easygui.fileopenbox()
    newfile = vrd.defaultpicsfolder + '/background_main.png'
    try:
        shutil.copy(file, newfile)
    except TypeError:
        pass


def sel_nw_path():
    path = easygui.diropenbox()  # Select path
    lis = []
    lis[:0] = path
    for i in range(len(lis)):
        if lis[i] == str('\\'):
            lis[i] = '/'
    new = "".join(lis)
    lis.clear()
    return new  


def dismantle_unicode_bars(string):
    lista = []
    lista[:0] = string

    for element in range(len(lista)):
        if lista[element] == '\\':
            lista[element] = '/'

    final_string = "".join(lista)
    return final_string


def edit_variables(index, new_value, pyfile):
    with open(vr.curr_vari_path, 'w+') as rw:
        pyfile[index] = new_value  # We stablish the specific line in pyfile and its value
        rw.writelines(pyfile)
        rw.close()


def read_variables():
    with open(vr.curr_vari_path, 'r') as d:
        pyfile = d.readlines()
    d.close()

    return pyfile


def variable_finder(new_var, current_var):
    vartxt = read_variables() 
    variables_list = []

    for i in range(len(vartxt)):  
        variables_list.append(vartxt[i].strip())

    for j in range(len(variables_list)):  
        if variables_list[j] != current_var:
            pass
        else:  # If we find our string
            indice = variables_list.index(variables_list[j])

            edit_variables(indice, new_var, vartxt)  
            break


def chg_dw_folder():
    defaultpath = dismantle_unicode_bars(vr.downloadpath)
    variable = 'downloadpath = ' + '"' + defaultpath + '"'  
    # print(variable)
    select_new_path = sel_nw_path()  
    new_path = 'downloadpath = ' + '"' + select_new_path + '/' + '"' + '\n'  
    variable_finder(new_path, variable)


def df_dw_folder():
    currentpath = vr.downloadpath
    defaulpath = vrd.downloadpath

    finalpath = dismantle_unicode_bars(defaulpath)
    variable = 'downloadpath = ' + '"' + currentpath + '"'
    new_path = 'downloadpath = ' + '"' + finalpath + '"' + '\n'
    variable_finder(new_path, variable)


def chg_bg_pic():
    sel_nwbg_path()


def open_folder(folder):

    for i in range(len(vrd.folders)):
        if folder == vrd.folders[1]:
            start = vrd.logfilespathos
        if folder == vrd.folders[2]:
            start = vr.downloadpath
        if folder == vrd.folders[3]:
            start = vrd.defaultpicsfolderos
        if folder == vrd.folders[4]:
            start = "C:/Program Files/DownPic.bat/"

    try:
        os.startfile(start)
    except UnboundLocalError:

        pass


def set_name_format(fileformat):

    new_formats = [' - ', '', '-', ' ']
    current_format = 'name_format = ' + '"' + vr.name_format + '"'
    for i in range(len(vrd.formats)):
        if fileformat == vrd.formats[1]:
            newformat = 'name_format = ' + '"' + new_formats[0] + '"' + '\n'
        if fileformat == vrd.formats[2]:
            newformat = 'name_format = ' + '"' + new_formats[1] + '"' + '\n'
        if fileformat == vrd.formats[3]:
            newformat = 'name_format = ' + '"' + new_formats[2] + '"' + '\n'
        if fileformat == vrd.formats[4]:
            newformat = 'name_format = ' + '"' + new_formats[3] + '"' + '\n'

    try:
        variable_finder(newformat, current_format)
    except UnboundLocalError:
        pass


def set_file_type(tipe):

    current_type = 'file_format = ' + '"' + vr.file_format + '"'
    for i in range(len(vrd.types)):
        if tipe == vrd.types[1]:
            new_type = 'file_format = ' + '"' + vrd.types[1] + '"' + '\n'
        if tipe == vrd.types[2]:
            new_type = 'file_format = ' + '"' + vrd.types[2] + '"' + '\n'
        if tipe == vrd.types[3]:
            new_type = 'file_format = ' + '"' + vrd.types[3] + '"' + '\n'

    try:
        variable_finder(new_type, current_type)
    except UnboundLocalError:
        pass


def print_file_format():
    new_formats = [' - ', '', '-', ' ']
    if vr.name_format == new_formats[0]:
        name_format = 'Picture - 1.jpg'
        return name_format
    if vr.name_format == new_formats[1]:
        name_format = 'Picture1.jpg'
        return name_format
    if vr.name_format == new_formats[2]:
        name_format = 'Picture-1.jpg'
        return name_format
    if vr.name_format == new_formats[3]:
        name_format = 'Picture 1.jpg'
        return name_format


def restore_def():
    shutil.copy(vrd.defa_vari_path, vrd.curr_vari_path)

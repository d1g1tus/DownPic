import os
import tkinter as tk
import webbrowser
import sys
sys.path.append('C:/Program Files/DownPic/')
from tkinter import ttk, font
from PIL import Image, ImageTk

import bin.functions.main_functions as mf
from bin.Data.variables import variables as vr
from bin.Data.variables import default_variables as vrd
from bin.functions import config_main_functions as cmf
from bin.guis import messages as ms


class FUNCTIONS:

    @staticmethod
    def update():
        root2.destroy()
        os.system("python " + vrd.config_path)


class BOTONES:

    @staticmethod
    def chg_bg_pic():
        ms.image_alert()
        cmf.chg_bg_pic()
        FUNCTIONS.update()

    @staticmethod
    def df_dnw_folder():
        cmf.df_dw_folder()
        FUNCTIONS.update()

    @staticmethod
    def img_folder():
        os.startfile(vrd.defaultpicsfolder)

    @staticmethod
    def set_name_style():
        selected = optionbartext.get()
        cmf.set_name_format(selected)
        FUNCTIONS.update()

    @staticmethod
    def open_folder():
        selected = optionbartext2.get()
        cmf.open_folder(selected)

    @staticmethod
    def chg_dnw_folder():
        cmf.chg_dw_folder()
        FUNCTIONS.update()

    @staticmethod
    def set_file_type():
        selected = optionbartext3.get()
        cmf.set_file_type(selected)
        FUNCTIONS.update()

    @staticmethod
    def help():
        git = 'https://github.com/d1g1tus/PicDown/blob/main/README.md'
        webbrowser.open(git)

    @staticmethod
    def licence():
        ms.licence()

    @staticmethod
    def restore_def():
        lol = 'Restore ALL Default Settings'
        answer = ms.confirm(lol)
        if answer is True:
            cmf.restore_def()
            FUNCTIONS.update()
        else:
            pass


root2 = tk.Tk()
nombre = "hola"

root2.title('DownPic Alpha 1.0 - Config')
root2.geometry(vrd.configwindowsize)
root2.resizable(0, 0)

bold = font.Font(weight="bold", size=10)

nb = ttk.Notebook(root2)
nb.pack(fill='both', expand='yes')

p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)

optionbartext = tk.StringVar()
optionbar = ttk.OptionMenu(p1, optionbartext, *vrd.formats).place(x=190, y=35)

optionbartext2 = tk.StringVar()
optionbar2 = ttk.OptionMenu(p1, optionbartext2, *vrd.folders).place(x=190, y=115)

optionbartext3 = tk.StringVar()
optionbar3 = ttk.OptionMenu(p1, optionbartext3, *vrd.types).place(x=190, y=75)

bg = 'light blue'

tk.Button(p1, text='Set Name Style', width=20, bg=bg, command=BOTONES.set_name_style).place(x=25, y=35)
tk.Button(p1, text='Open Folder', width=20, bg=bg, command=BOTONES.open_folder).place(x=25, y=115)
tk.Button(p1, text='Set File Type', width=20, bg=bg, command=BOTONES.set_file_type).place(x=25, y=75)
tk.Button(p1, text='Restore ALL Default Settings', width=25, bg=bg, command=BOTONES.restore_def).place(x=25, y=165)

header = 'CURRENT                  DEFAULT'
ttk.Label(p1, text=header, font=bold).place(x=328, y=10)

name_format = cmf.print_file_format()
ttk.Label(p1, text=name_format).place(x=320, y=35)
ttk.Label(p1, text='Picture - 1.jpg').place(x=455, y=35)

ttk.Label(p1, text=vr.file_format).place(x=345, y=75)
ttk.Label(p1, text=vrd.file_format).place(x=480, y=75)

tk.Button(p2, text='Change Download Folder', width=30, bg=bg, command=BOTONES.chg_dnw_folder).place(x=40, y=45)
tk.Button(p2, text='Default Download Folder', width=30, bg=bg, command=BOTONES.df_dnw_folder).place(x=40, y=115)
ttk.Label(p2, text='Default Path -> ' + vrd.downloadpath).place(x=40, y=90)
ttk.Label(p2, text='Current Path -> ' + cmf.dismantle_unicode_bars(vr.downloadpath)).place(x=40, y=20)

tk.Button(p3, text='Change PicDown Background', width=30, bg='light blue', command=BOTONES.chg_bg_pic).place(x=40, y=75)
tk.Button(p3, text='Open Images Folder', width=30, bg='light blue', command=BOTONES.img_folder).place(x=40, y=115)

img = Image.open(vrd.backgroundpic)
resized_image = img.resize((170, 150), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

tk.Label(p3, image=new_image).place(x=325, y=25)
tk.Label(p3, text='IMAGE PREVIEW', font=bold).place(x=360, y=185)

tk.Button(p4, text='Help - How to Guide', width=20, bg=bg, command=BOTONES.help).place(x=20, y=45)
tk.Button(p4, text='Licence', width=20, bg=bg, command=BOTONES.licence).place(x=20, y=75)
tk.Label(p4, text='HELP & ABOUT', font=bold).place(x=47, y=10)

nb.add(p1, text='INDEX')
nb.add(p2, text='PATHS')
nb.add(p3, text='IMAGES')
nb.add(p4, text='HELP / ABOUT')

root2.mainloop()

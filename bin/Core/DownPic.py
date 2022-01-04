import shutil
import tkinter
import tkinter as tk
import os
import easygui
import sys
sys.path.append('C:/Program Files/DownPic/')

from tkinter import messagebox
from tkinter import font
from bin.functions import main_functions as mf
from bin.guis import messages as ms
from pynput.mouse import Listener
from bin.Data.variables import variables as vr
from bin.Data.variables import default_variables as vrd


current_file = vr.today_txt_file

mf.declare_download_def_path()
mf.folder_exist_check(vr.logfilespath)
mf.file_exist_check(vr.txt_file_name, vr.logfilespath)


class FUNCIONES:
    nomodlog = bool(False) 

    @staticmethod
    def dephvariables(link, eman, v1ar, v2ar, hoy):

        if eman != 'Name':
            pass
        else:
            eman = 'Picture'

        headervariables = [link, eman, v1ar, v2ar, hoy]

        if v1ar == 'Var1':
            if v2ar == 'Var2':
                headervariables = [link, eman, hoy]
            else:
                headervariables = [link, eman, v2ar, hoy]
        else:
            if v2ar == 'Var2':
                headervariables = [link, eman, v1ar, hoy]

        return headervariables

    @staticmethod
    def print_txt():
        with open(vr.today_txt_file, 'r') as hola:
            keep = hola.readlines()

        for i in range(len(keep)):
            loglist.insert(tk.END, keep[i])
            loglist.see(tk.END)

    @staticmethod
    def print_oldlog(text):
        for i in range(len(text)):
            loglist.insert(tk.END, text[i])
            loglist.see(tk.END)


class BOTONES:

    @staticmethod
    def start():
        if FUNCIONES.nomodlog is False:
            if vr.pot == 1:
                global fulla
                vr.linklist.clear()  
                vrd.opt = bool(True)
                fulla = tk.Toplevel(root)
                fulla.protocol("WM_DELETE_WINDOW", mf.disable_item)
                fulla.geometry('300x100')
                fulla.resizable(0, 0)
                fulla.title('Link Collector')
                label = tkinter.Label(fulla, text='Program waiting for link inputs')
                label.pack()
                vr.pot = 2
                vrd.mousewhisperer = bool(True)
                Listener(on_click=mf.on_click).start()
            else:
                pass
        else:
            ms.old_logs()

    @staticmethod
    def stop():
        if vr.pot == 2:
            global fulla
            fulla.destroy()
            vrd.mousewhisperer = bool(False)
            vrd.opt = bool(False)
            vr.pot = 1
            mf.write_links_txt(vr.linklist) 
            FUNCIONES.print_txt()  
            BOTONES.todayslog()
        else:
            ms.stop_twice()

    @staticmethod
    def config():
        os.system(vrd.open_config)

    @staticmethod
    def export():
        try:
            folder = easygui.diropenbox()
            shutil.copy(current_file, folder)
            ms.exported()
        except TypeError:
            pass

    @staticmethod
    def todayslog():
        global current_file
        loglist.delete(0, tk.END)
        FUNCIONES.print_txt()
        FUNCIONES.nomodlog = bool(False)  
        current_file = vr.today_txt_file

    @staticmethod
    def loadreg():
        try:
            global current_file
            file = easygui.fileopenbox()
            loglist.delete(0, tk.END)
            FUNCIONES.nomodlog = bool(True)
            m = mf.read_txt(file)
            current_file = file
            # print(current_file)
            FUNCIONES.print_oldlog(m)
        except TypeError:
            pass

    @staticmethod
    def downloads():
        ms.downloadstartin()
        mf.write_auto_keep(current_file)
        mf.write_line_auto_keep(current_file)
        mf.download_manager_links(current_file)
        vr.downloadedlinks.clear()
        mf.txt_after_download(current_file)
        ms.downloadfinish()

    @staticmethod
    def clearallreg():
        out = tkinter.messagebox.askyesno(message='Are you sure you want to delete ALL logs?', title='WARNING!!!')
        if out is True:
            try:
                os.remove(vr.pathautokeep)
                os.remove(vr.today_txt_file)
                loglist.delete(0, tk.END)
            except FileNotFoundError:
                msj = 'All log files have been deleted. Nothing else to delete.'
                tk.messagebox.showinfo(title="ATENTION", message=msj)
                pass
        else:
            pass

    @staticmethod
    def setparameters():
        if FUNCIONES.nomodlog is False:

            link = 'GROUP'
            name = namebox.get()
            var1 = var1box.get()
            var2 = var2box.get()

            listavariables = FUNCIONES.dephvariables(link, name, var1, var2, vr.hoy)
            mf.write_group_header(listavariables)
            BOTONES.todayslog()

        else:
            ms.old_logs()

    @staticmethod
    def salir():
        try:
            os.remove(vr.pathautokeep)
        except FileNotFoundError:
            pass
        root.destroy()

root = tk.Tk()

root.title('PicDown - Alpha 1.0')

root.geometry(vr.mainwidowsize)
root.resizable(0, 0)

fuente = font.Font(weight='bold')
backgroundpic = tk.PhotoImage(file=vr.backgroundpic)

fotofondo = tk.Label(root, image=backgroundpic)

msgbox = tk.StringVar()
namebox = tk.StringVar()
namebox.set("Name")
var1box = tk.StringVar()
var1box.set("Var1")
var2box = tk.StringVar()
var2box.set("Var2")

tpname = tk.Entry(root, textvariable=namebox, width=15)
tpvar1 = tk.Entry(root, textvariable=var1box, width=15)
tpvar2 = tk.Entry(root, textvariable=var2box, width=15)

msgboxframe = tk.Frame(root)
nameboxframe = tk.Frame(root)
var1boxframe = tk.Frame(root)
var2boxframe = tk.Frame(root)


scrollbar = tk.Scrollbar(msgboxframe)

loglist = tk.Listbox(msgboxframe, height=22, width=95, yscrollcommand=scrollbar.set)
namelist = tk.Listbox(nameboxframe, height=7, width=30)
var1list = tk.Listbox(var1boxframe, height=7, width=30)
var2list = tk.Listbox(var2boxframe, height=7, width=30)

FUNCIONES.print_txt()

setnamebt = tk.Button(root, text=('SET'+'\n'+'PARAMETERS'), heigh=3, width=10, command=BOTONES.setparameters)
download = tk.Button(root, text='Download', height=1, width=10, command=BOTONES.downloads)
start = tk.Button(root, text='Start', height=1, width=10, command=BOTONES.start)
stop = tk.Button(root, text='Stop', height=1, width=10, command=BOTONES.stop)
config = tk.Button(root, text='Configuration', height=1, width=23, command=BOTONES.config)
bthelp = tk.Button(root, text='Export Current Log File', height=1, width=23, command=BOTONES.export)
savereg = tk.Button(root, text="Today's Log", height=1, width=15, command=BOTONES.todayslog)
loadreg = tk.Button(text='Load Registry', height=1, width=15, command=BOTONES.loadreg)
clearallreg = tk.Button(text='Clear All Registry', height=1, width=15, command=BOTONES.clearallreg)
buttonexit = tk.Button(root, text='Exit', height=1, width=10, command=BOTONES.salir)

fotofondo.place(x=0, y=0)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

loglist.pack(fill=tk.BOTH)
msgboxframe.place(x=15, y=15)

namelist.pack()
tpname.place(x=15, y=385)

var1list.pack()
tpvar1.place(x=15, y=418)

var2list.pack()
tpvar2.place(x=15, y=450)

setnamebt.place(x=120, y=382)
download.place(x=120, y=450)
start.place(x=215, y=382)
stop.place(x=305, y=382)
config.place(x=215, y=416)
bthelp.place(x=215, y=450)
savereg.place(x=400, y=382)
loadreg.place(x=400, y=416)
clearallreg.place(x=400, y=450)
buttonexit.place(x=525, y=416)

root.mainloop()


import tkinter as tk

from tkinter import messagebox
from bin.Data.variables import default_variables as vrd

def exported():
    msj = 'Your log file has been exported successfully.'
    tk.messagebox.showinfo(title="LOGFILE SUCCESSFULLY EXPORTED", message=msj)

def confirm(action):
    msj = 'Are you sure do you want to ' + action + ' ? '
    msj2 = 'This action cannot be undone'
    msjtotal = msj + msj2
    answer = tk.messagebox.askyesno(title='Confirmation Required', message=msjtotal)
    return answer

def licence():
    a1 = "You're only allowed to use this code privately. "
    a2 = "You can change it and use it in anyway you want, as long as you keep it private. "
    a3 = "I do not take any responsability in any change you may apply nor any unethical use. "
    msj = (a1 + a2 + a3)
    tk.messagebox.showinfo(title="Licence", message=msj)

def image_alert():
    msj = 'Take into account that ONLY pics with a ' + vrd.mainwidowsize + ' res AND PNG extension are accepted.'
    tk.messagebox.showinfo(title="ATENTION", message=msj)

def old_logs():
    msj = 'This is an old log, and you cannot edit old logs. What is done cannot be undone'
    tk.messagebox.showinfo(title="ATENTION", message=msj)


def downloadfinish():
    msj = 'Downloads have been completed.'
    tk.messagebox.showinfo(title="ATENTION", message=msj)


def downloadstartin():
    msj = '''Download is in progress. This might take a few seconds/minutes. Please be patient. Press Accept
    to proceed'''
    tk.messagebox.showinfo(title="ATENTION", message=msj)

def downnameerror():
    msj = 'Apparently you have not selected any log file. Please select one...'
    tk.messagebox.showinfo(title="ATENTION", message=msj)


def nologsel():
    msj = '''Apparently there are no links on your log. Nothing has been downloaded but folders have been' \
          created if there were none. '''
    tk.messagebox.showinfo(title="ATENTION", message=msj)


def stop_twice():
    msj = "You can't cancel twice bro..."
    tk.messagebox.showinfo(title="ATENTION", message=msj)
    

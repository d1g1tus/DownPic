import os
from datetime import date

'''
VARIABLES NO MODIFICABLES Y PREDEFINIDAS
'''
# STATIC DATA
mainwidowsize = '950x500'
configwindowsize = '550x250'

# PATHS FIJAS
vari_folder = "C:/Program Files/DownPic/bin/Data/variables/"
defa_vari_name = 'default_variables.py'
defa_vari_path = vari_folder + defa_vari_name
curr_vari_name = 'variables.py'
curr_vari_path = vari_folder + curr_vari_name

config_path = '"C:/Program Files/DownPic/bin/Core/config.py"'
open_config = 'python ' + config_path

# DATE - TIME
hoy = str(date.today())
today = str(date.today())

# TIMES / WATCHES / TRIGGERS
pot = 1
rmcounter = 0
rlcounter = 0

# LISTAS
types = ['Select type', '.jpg', '.png', '.gif']
formats = ['Select format', 'Default', 'Picture1.jpg', 'Picture-1.jpg', 'Picture 1.jpg']
folders = ['Select Folder', 'Logs', 'Downloads', 'Images', 'Install Folder']
linklist = []
headers1 = []
headers2 = []
downloadedlinks = []
rutas = []

# BOOLEANS
mouseholder = bool(False)  # Sirve para el juego de ifs del boton izq-der-izq
mousewhisperer = bool(False)  # Sirve para que se active el hotkey del ratón
firstlink = bool(True)  # Comprueba si el link copiado es el primer link copiado del día
opt = bool(True)
permdesc = bool(False)  # Sirve para permitir las descargas totales sin division de bloques
config_bool = bool(False)

# RAW DATA
line = '------------------------------------------------------------------------------\n'
linename = '------------------------------------------------------------------------------'

'''
VARIABLES MODIFICABLES Y PREDEFINIDAS
'''
# Ruta de acceso a Logs
logfilespath = os.environ.get('USERPROFILE') + '/Logs/'
logfilespathos = '"' + os.environ.get('USERPROFILE') + '/Logs/' + '"'

# Nombre del log del día HOY y ruta
txt_file_name = str(today + ' - log.txt')
today_txt_file = logfilespath + txt_file_name

# Nombre del autolog (el que sea) y su ruta
autokeep_txt_file = str('Auto-' + txt_file_name)
pathautokeep = logfilespath + autokeep_txt_file

'''
VARIABLES MODIFICABLES 
'''
# BACKGROUND PICTURES
backgroundpic = "C:/Program files/DownPic/bin/Data/Images/background_main.png"
defaultpicsfolder = "C:/Program files/DownPic/bin/Data/Images/"
defaultpicsfolderos = '"C:/Program files/DownPic/bin/Data/Images/"'

downloadpath = "C:/Users/CASH/Downloads/"
# Name File Format
name_format = " - "
file_format = ".jpg"

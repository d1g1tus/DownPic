# DownPic - Alpha 1.0



### Downloading and Installing DownPic
----------------------------------------------------

__1. Option__ -> *Download an Installer*

I'm currently working on this feature. It will be available soon

__2. Option__ -> *Download the whole repository as Zip*

❗❗❗ ⚠ __Main installation path HAS TO BE the following ->__ "C:\Program Files\DownPic\" ⚠ ❗❗❗

*Otherwise DownPic won't work. Converserly, you might change default paths on "Default_Variables" and "Variables" to fit your preferences*



### Set Up - Running DownPic
-----------------------------------------------------

__Running DownPic__ is quite simple. You only need to run python command on shell with the following default path: 

"C:/Program Files/DownPic/Launcher - DownPic.py"

So, for the __Setup__ you could create your own bat, to run launcher.py or use my Setup.bat. 

--------------------------------------------------------
-------------------------------------------------------
# A SIMPLE HOW TO FOR DOWNPIC

### MAIN FEATURES

![alt text](https://i.ibb.co/M99Tkb0/Main1.png)

__1. Name, Var1 and Var2__ -> These are some input vars for the final user to use in order to classify their downloads. If non set they will not be added. Adittionally, these vars are used to name each download directory. By default any set of links will have a header with the following static vars:

 - GROUP -> It is use only for the sake of order. 
 - Picture -> This is the default name that will be assignated for folders and files in case no name is given. 
 - Date -> This will be the final download folder, and where all the pictures will actually be downloaded.

__2. Set Parameters__ -> This button will append "Name, Var1 and Var2" as a header to the current log.txt file. You can have as many headers as you want, even if they hold no links. Folders will still be created but no file will be downloaded inside them.

__3. Download__ -> This button will make a pop-up information window to appear, just for the user to know everything's correct and that downloading is about to begin. You have to press Accept in order to start downloading files. While the process is on DownPic will probably freeze until it's over, and another pop-up window appears to indicate that all files have been successfully retrieved. 

__4. Start__ -> This button will make a pop-up information window to appear, just for the user to know that DownPic is currently listening to our mouse activity. The main usage of this feature has to follow this secuence:

 - *RIGH CLICK* -> Press right mouse button on any picture you would like to download. It should work with almost any image, but if any issue arises I extremely recommend searchinf for the original source of the picture and then right clicking it. 
 
 - *LEFT CLICK* -> Since you have to press firstly right click over an image, a context menu will have appeared. Now you have to press left mouse button over "Copy Image URL". This will freeze DownPic for 0.4 seconds and append that link to the current Log.txt file. 

Take into account that if you press right button randomly this secuence will be triggered anyway. If no url has been selected the program will ignore the input. If the latest used url is still on the clipboard DownPic will notify you that the link copied is already in list and will not be appended. 

__5. Stop__ -> This stops Mouse Listener and definately appends all urls to Log.txt file. If you press it twice a window will pop-up to prevent rewriting Log.txt file with the same links. If you want to make sure all urls are saved and to regain control of your mouse, press it. 

__6. Configuration__ -> This runs a separated Configuration Window that will be completely explained further below. 

__7. Export Current Log File__ -> A simple button to save the current log file that DownPic is displaying and keep it elsewhere. This also works with loaded log files. 

__8. Today's Log__ -> Quickly Reload of Today's Log. It is also useful in case DownPic is having problems with Log.txt editing and you want to make sure what DownPic is displaying is what's actually written on Log.txt.

__9. Load Registry__ -> This will load any Log file (any txt file in reality). Any editing feature will be blocked and you will only be able to read it, Download its content and Export it. 

This feature, along with *Export Current Log File* are meant to be used as a way to share Logs between users and create a new easier way to share files. Instead of sending tons of pictures, you can simply send a txt and run DownPic. 

__10. Clear all registry__ -> This will delete ALL files inside /Logs/. 

__11. Exit__ -> If you encounter any strange or odd issue while closing DownPic, it should be prevented by using exit button. 




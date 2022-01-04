# DownPic - Alpha 1.0

## IMPORTANT PREVIOUS CONSIDERATIONS 
--------------------------------------

DownPic is JUST a Download Manager. It is not intended to be used with any other purpouse. It is not intended to be used as a File Manager, so please do not ask any implementation related to such matters. 

DownPic basically is able to create a Log file, following precise specifications, write on it, read it, and download images urls storing them in New Folders created following every Header information. 

--------------------------------------

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

So, for the __Setup__ you could create your own bat, to run launcher.py or use my Launcher.bat. 

-------------------------------------------------------

# A SIMPLE HOW TO FOR DOWNPIC

--------------------------------------------------------

### MAIN FEATURES

--------------------------------------------------------

![alt text](https://i.ibb.co/M99Tkb0/Main1.png)

__1. Name, Var1 and Var2__ -> These are some input vars for the final user to use in order to classify their downloads. If non set they will not be added. Adittionally, these vars are used to name each download directory. By default any set of links will have a header with the following static vars:

 - GROUP -> It is use only for the sake of order. 
 - Picture -> This is the default name that will be assignated for folders and files in case no name is given. 
 - Date -> This will be the final download folder, and where all the pictures will actually be downloaded.

__2. Set Parameters__ -> This button will append "Name, Var1 and Var2" as a header to the current log.txt file. You can have as many headers as you want, even if they hold no links. Folders will still be created but no file will be downloaded inside them.

❗❗ If you don't want to use an specific var, simply do not change its content. In case you did, just write "Name, Var1, Var2" again. 

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

------------------------

### CONFIGURATION

--------------------------------------------------------

### Index

--------------------------------------------------------

![alt text](https://i.ibb.co/SP81Hx4/1.png)

__1. Set Name Style + Select Format__ -> This options are related with the final name format the downloaded picture will have. There are several options for you to choose. 

![alt text](https://i.ibb.co/CWJjQ0G/2.png)

__2. Set File Type__ -> DownPic currently is not able to tell the difference amongst the files it downloads, so instead it names every file with just one single format. Currently it only works with jpg, png and gif. 

![alt text](https://i.ibb.co/xLyHr2j/3.png)

__3. Open Folder__ -> Pretty self-explanatory. 

![alt text](https://i.ibb.co/MMDggcD/4.png)

--------------------------------------------------------

### Paths

--------------------------------------------------------

![alt_text](https://i.ibb.co/xFxMHvJ/5.png)

__1. Change Download Folder__ -> This will change the Download Path DownPic follows. However, all images will always be downloaded in ./GROUP/

__2. Default Download Folder__ -> This resets Download path to %USERPROFILE%/Downloads

--------------------------------------------------------

### Images

--------------------------------------------------------

![alt_text](https://i.ibb.co/WgvQ7J6/6.png)

__1. Change DownPic Background__ -> Take into account that __ONLY PNG IMAGES WITH A 950x500 RES__ are accepted. You can use any other size but it won't fit. Use any online resource to change your Background resolution before adding it.

__2. Open Images Folder__ -> Just a short cut to Images DownPic folder. This is NOT the DOWNLOADS folder. 

--------------------------------------------------------

### Help / About

--------------------------------------------------------

![alt_text](https://i.ibb.co/169z81Z/7.png)

__1. Help - How to Guide__ -> This is one of the many possible ways in which you arrived here. 

__2. Licence__ -> Pretty short disclaimer about DownPic's Licence

--------------------------------------------------------

# ❗❗❗ ⚠ SOME OTHER IMPORTANT CONSIDERATIONS ⚠ ❗❗❗

--------------------------------------------------------

### Editing the Log file with a notepad

--------------------------------------------------------

It's a real fact. You could basically ignore DownPic features completely, and as long as you follow the Log.txt format rules you could still load your "homebrew" log file and DownPic still would be able to download everything you wrote down. This is particularly interesting if you want to share your ImgBB or personal album with someone, but you have too many images to be sent all together. 

❗❗❗ Actually a future version of DownPic will include a Log file modification feature to avoid using any other program. 

**NOTEPAD FORMAT**

![alt_text](https://i.ibb.co/chp8ZRQ/8.png)

 - *Line 2* -> GROUP is a static Value and has to remain unchanged. From there, you can add up to 4 different variables. You don't have to write the 4 of them, but "Picture" var has to include any kind of value for this will be used for naming the downloaded files. 
 
 - *Line 3* -> It is __IMPERATIVE__ that you use the __EXACT SAME NUMBER__ of "-", because otherwise it won't work.

❗❗❗ Here you have the Line -> ------------------------------------------------------------------------------
 
 - *Line 5* -> Here you can append as many urls as you want. Just 1 url per line. It does not matter if 1 link occupies for than 1 line.
 
 - *Line 6* -> It doesn't have to be exactly line 6, it could be any line. I just mention it to ensure that you add '\n' just on the last URL of your list. 

This would lead to a final result similar to this:

![alt_text](https://i.ibb.co/9yfcZNX/9.png)

And if you would like to keep adding headers just follow the same steps, and append all the information on the txt. DownPic will read the entire file and download any link!

--------------------------------------------------------

### DownPic + Refreshing Changed Data

--------------------------------------------------------

Sometimes you will have to restart DownPic, because otherwise the program will not be able to read changes applied to global vars and it might not apply the changes you have just done. However this does not occur everytime. 

--------------------------------------------------------

### DownPic - Downloading Restricted Content / Unreachable Urls

--------------------------------------------------------

DownPic has some in-built methods to bypass certain "anti-bots" requests online blockers. However it will not be able to download very specific URLS, such as those protected with passwords, or those which require a Key.

--------------------------------------------------------

# ❗❗❗ SOCIAL NETWORKS, WAYS OF CONTACT ❗❗❗

--------------------------------------------------------

Right now I only use Github. Use this platform to contact me if you have any doubt or if you want to collaborate. 

--------------------------------------------------------

# ❗❗❗ ⚠ LICENCE ⚠ ❗❗❗

--------------------------------------------------------

- You're only allowed to use this code privately. 
- No lucrative use of any sort of this code is allowed
- You can change it and use it in anyway you want, as long as you keep it private. 
- I do not take any responsability in any change you may apply nor any unethical use.


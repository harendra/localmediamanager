LocalMediaManager
=================

Simple Application to manage your local media (videos) using browser interface. Really handy if you
use chromecast. Just use the application with chrome with chromecast extension installed, you are ready
to stream all your content right from browser.

Introduction
===============
LocalMediaManager is a python application (python 2.7) that scans specified folders (and subfolders) for media files and indexes them. While indexing it takes
several screenshots of all the files found and dumps all the information in a json file. You can then just open index.html file and manage all your media through browser. No installation required.

Features
=================
1. Scans the media files from specified folders.
2. Uses Qt4 user interface.
3. Generates tags automatically.
4. Ability to search all the media through browser.
5. Plenty of screenshots of video spanning from beginning to end using ffmpeg (included). Can display only few or all images.
6. All the videos can be played right on the browser. Just open video link on new tab.
7. No server installation required (can be used with a web server as well). All the index is saved as json file.
8. Records view history in browser local storage so you can keep track of what you have watched.
9. Great if you use chromecast!

Opera and chrome are recommended browsers.

View wiki,
https://github.com/harendra/localmediamanager/wiki

Screenshot,
https://raw.github.com/harendra/localmediamanager/master/LocalMediaManager/web/assets/img/homemediascreen.jpg



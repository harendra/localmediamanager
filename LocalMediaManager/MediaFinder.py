'''
Created on 18 Jul 2013

@author: harendra
'''
import os
from collections import Counter
import re
import subprocess
import datetime
import os
class MediaFinder(object):
    foundfiles = {}
    allfiles = []
    rootfolder = "web\\assets\\img\\thumbnails"
    rootfolders=None
    customstopwords = "tagsetting\\stopwords"
    defaultstopwords = os.path.join(os.path.abspath("."),"tagsetting/defaultstopwords")
    ffmpegfolder = os.path.join(os.path.abspath("."),"ffmpeg")
    currentfolder = 1
    timing = [1, 2, 3, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 96, 97, 98, 99]
    jsonfile = os.path.join(os.path.abspath("."),"web/assets/js/json.js")
    tagsfile = os.path.join(os.path.abspath("."),"web/assets/js/tags.js")
    rootfoldersfile=os.path.join(os.path.abspath("."),"web/assets/js/root.js")
    
    def __init__(self,rootfolders,customstopwords,updateobject,callback):
        self.rootfolders=rootfolders
        if len(customstopwords.strip())!=0:
            self.customstopwords=customstopwords
        self.updateobject=updateobject
        self.callback=callback
        #write selected root folders to javascript
        self.addRootFolders()
        self.searchForMedia(self.rootfolders)
    
    def addRootFolders(self):
        self.writeFile(self.rootfoldersfile, "var rootfoldersfile="+str(self.rootfolders))        
    
    def writeFile(self,filename,content):
        f=open(filename,"w")
        f.write(content)
        f.close()
            
    def searchForMedia(self, rootfolders):
        mediaIndexList = {}
        for key in rootfolders:
            rootfolder = key
            self.foundfiles = {}
            foundFilesCurrent = self.parseDirectory(rootfolder)
            mediaIndexList[key] = self.foundfiles
        f = open(self.jsonfile, "w")
        f.write("allfiles=" + str(mediaIndexList))
        f.close()
        
        customtags = []
        _customtags = []
        for customtag in customtags:
            if customtag[0] != '#':
                _customtags.append(customtag.strip())
        tags = self.createKeywords(str(self.allfiles))        
        f = open(self.tagsfile, "w")
        f.write("tags=" + str(tags))
        f.close()
        
        self.callback(self.updateobject,"Indexing complete! Start web/html/index.html on your web browser")

    def getWordList(self, filename):
        customtags = open(filename).readlines()
        _customtags = []
        for customtag in customtags:
            if customtag[0] != '#' and len(customtag) != 0:
                _customtags.append(customtag.strip())
        return _customtags        
        
    def parseDirectory(self, directory):
        if directory.find(self.rootfolder) != -1:
            return
        try:
            dirs = os.listdir(directory)
        except:
            return
        dirlist = []
        for dir in dirs:
            path = os.path.join(directory, dir)
            dirlist.append(path)
        self.foundfiles[directory] = {'type':'directory', 'filelist':dirlist, 'parent':os.path.dirname(directory)}
        for path in dirlist:
            if os.path.isfile(path):
                if(path.find(".mkv") != -1 or path.find(".wmv") != -1 or path.find(".avi") != -1 or path.find(".mp4") != -1):
                    thumbnails = self.createThumbnails(path)
                    self.foundfiles[path] = {'type':'file', 'filelist':thumbnails, 'parent':os.path.dirname(path), 'filetype':'video'}
                    self.allfiles.append(str(os.path.basename(path)))
                    parentdir = os.path.basename(os.path.dirname(path))
                    self.allfiles.append(parentdir)
                pass
            else:
                self.callback(self.updateobject,"Currently processing " + path)
                self.parseDirectory(path)
        return
    
    def createThumbnails(self, filepath):
        folder = os.path.join(self.rootfolder, os.path.basename(filepath))
        write = True
        self.currentfolder += 1
        try:
            os.mkdir(folder)
        except:
            write = False
        thumbnaillist = self.generateThumbnails(filepath, folder + "\\", write)
        return thumbnaillist
    

    def generateThumbnails(self, filename, outputfolder, write):
        thumbnailfiles = []
        ffprobecommand=os.path.join(self.ffmpegfolder,"ffprobe.exe")
        ffmpegcommand=os.path.join(self.ffmpegfolder,"ffmpeg.exe")
        p = subprocess.Popen([ ffprobecommand, '-i', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        output = str(p[1])
        tokens = output.split("\n")
        duration = ""
        for token in tokens:
            if token.find('Duration') != -1:
                streamtokens = token.split(" ")
                duration = streamtokens[3].strip().replace(",", "")
        try:
            seconds = self.getseconds(duration)
        except:
            return thumbnailfiles
        outputfilenameprefix = "screenshot"
        for t in self.timing:
            outputfilename = outputfolder + outputfilenameprefix + str(t) + ".jpg"
            thumbnailfiles.append(outputfilename)
            currentposition = (seconds / 100) * t            
            time = str(datetime.timedelta(seconds=int(currentposition)))
            if write:
                p = subprocess.Popen([ ffmpegcommand, '-ss', time, '-i', filename, '-vframes', '1', outputfilename], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()        
        return thumbnailfiles
    
    def getseconds(self, strtime):
        l = strtime.split(':')
        return float(l[0]) * 3600 + float(l[1]) * 60 + float(l[2])

    def createKeywords(self, text):
        text=text.replace("'","").replace("[","").replace(",","").replace("."," ")
        textstuff = text.split(' ')
        _digits = re.compile('\d')
        _nonalpha = re.compile('\W')
        for textword in textstuff:
            if bool(_digits.search(textword)) or bool(_nonalpha.search(textword)):
                text = text.lower().replace(textword.lower(), ' ')                
        mystopwords = self.getWordList(self.customstopwords)
        for word in mystopwords:
            text = text.lower().replace(word.lower(), '')
        splitwords = text.split(" ")
        ignored_words = []
        mystopwords += ignored_words
        stopwords = self.getWordList(self.defaultstopwords)
        mystopwords += stopwords
        newsplitwords = []
        for word in splitwords:
            skip = False
            for stopword in mystopwords:
                if word.strip().lower() == stopword or len(word) < 3 or word.find('_') != -1 or bool(_digits.search(word)) or bool(_nonalpha.search(word)):
                    skip = True
            if not skip:
                newsplitwords.append(word)
        c = Counter(newsplitwords)
        bestmatches = c.most_common()
        matches=[]
        for match in bestmatches:
            matches.append(match[0])
        return matches    
        

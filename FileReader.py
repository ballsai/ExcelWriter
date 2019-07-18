import re
import os

class FileReader:
    
    def __init__(self,path):
        self.path = path
        self.details = []
        self.lines = []
        self.stringList = []
        self.hostname = ''

    def readFile(self):
        try:
            with open(self.path, 'r') as f:
                self.lines = list(line for line in (l.strip() for l in f) if line)     # read file without blank lines
        except IOError:
            print('Path does not exist')

    def getDetail(self, labelName, substring):
        temp = []
        temp.append(labelName)
        for line in self.lines:
            if re.search(keyword, line):
                temp.append(re.sub(substring,'',line))
                self.details.append(temp)
                break

    def getHostname(self):
        filename = os.path.basename(self.path)
        self.hostname = re.split(r',| |_[0-9][0-9]\.', filename)[0]
    
    def initDict(self):
        _dict[self.hostname] = []
    
    def splitString(self, subString):
        splitStringList = []
        for string in self.stringList:
            splitStringList.append(re.split(subString,string))
            self.stringList = splitStringList

    def getStringList(self, startSubstring, endSubstring):
        betweenSubstring = False
        for line in self.lines:
            if re.search(startSubstring, line):
                betweenSubstring = True
                continue
            elif re.search(endSubstring, line):
                betweenSubstring = False
                break
            elif betweenSubstring:
                # ls.append(re.split(r'\s{2,}',line))
                self.stringList.append(line)
        return self.stringList



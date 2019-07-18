import re
import os
import codecs

class FileReader:
    
    def __init__(self,path):
        self.path = path
        self.lines = []
        self.string_list = []
        self.hostname = ''

    def readFile(self):
        try:
            with open(self.path, 'r', encoding='utf-8', errors='ignore') as f_in:   # open file
                self.lines = list(filter(None, (line.rstrip() for line in f_in)))   # read file all lines except blank lines
        except IOError:
            print('Can not read file / file not found')

    def getHostname(self):
        filename = os.path.basename(self.path)
        self.hostname = re.split(r',| |_[0-9][0-9]\.', filename)[0]
    
    def splitString(self, substring):
        split_string = []
        for string in self.string_list:
            split_string.append(re.split(substring,string))
        return split_string

    def getStringList(self, start_substring, end_substring):  # get string/text between substrings
        betweenSubstring = False
        for line in self.lines:
            if re.search(start_substring, line): # start substring / first line to read
                betweenSubstring = True
                continue
            elif re.search(end_substring, line): # end substring  / last line to read then break 
                betweenSubstring = False
                break
            elif betweenSubstring: 
                self.string_list.append(line) # store string each line in string_list
        return self.string_list



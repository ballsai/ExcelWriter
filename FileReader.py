import re

class FileReader:
    def __init__(self,path):
        self.path = path
        self.details = []
        self.lines = []

    def readLines(self):
        try:
            with open(self.path, 'r') as f:
                self.lines = list(line for line in (l.strip() for l in f) if line)
        except IOError:
            print('Path does not exist')

    def getDetail(self, header_name, keyword):
        temp = []
        temp.append(header_name)
        for line in self.lines:
            if re.search(keyword, line):
                temp.append(re.sub(keyword,'',line))
                self.details.append(temp)
                break


    def findText(self, start, end):
            readColumn = False
            readBetweenLines = False
            ls = []
            for line in self.lines:
                if re.search(start, line):
                    readColumn = True
                    readBetweenLines = True
                    continue
                elif re.search(end, line):
                    readBetweenLines = False
                    break
                elif readColumn:
                    ls.append(line.split())    
                    readColumn = False
                    continue
                elif readBetweenLines:
                    ls.append(re.split(r'\s{2,}',line))
            return ls


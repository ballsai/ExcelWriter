import re

class FileReader:
    def __init__(self,path):
        self.path = path
        self.lines = []

    def readLines(self):
        try:
            with open(self.path, 'r') as f:
                self.lines = list(line for line in (l.strip() for l in f) if line)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise


    def findDetail(self):
        for line in self.lines:
            if re.search('.*#show ver.*', line):
                print(re.sub('#show version','',line))
            elif re.search('^Model ([n]|[N])umber.*:', line):
                print(re.sub('^Model ([n]|[N])umber.*:','',line))

    def findText(self, start, end):
            column = False
            between = False
            ls = []
            for line in self.lines:
                if re.search(start, line):
                    column = True
                    between = True
                    continue
                elif re.search(end, line):
                    between = False
                    continue
                elif column :
                    ls.append(line.split())
                    column = False
                elif between:
                    ls.append(re.split(r'\s{2,}',line))
            return ls
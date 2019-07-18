from glob import glob
import os

class FileList:
    def __init__(self, _dir, regex):
        self._dir = _dir
        self.regex = regex
        self.pathList = []

    def listOfFiles(self):
        self.pathList = glob(self._dir+self.regex)
        return self.pathList
    

from glob import glob
import os

class FileList:
    def __init__(self, _dir, substring):
        self._dir = _dir    # directory name
        self.substring = substring  # filename substring
        self.path_list = [] # list of paths

    def getFileList(self):
        self.path_list = glob(self._dir+self.substring) # find matching files path
        return self.path_list
    

from glob import glob

class FileList:
    def __init__(self, _dir, filename):
        self._dir = _dir
        self.filename = filename

    def listOfFiles(self):
        fl = glob(self._dir+self.filename)
        return fl
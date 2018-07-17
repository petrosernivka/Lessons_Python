#https://www.codewars.com/kata/file-path-operations
class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath[len(self.filepath)-len(self.filepath)+self.filepath.find('.')+1:]
    def filename(self):
        return self.filepath[-len(self.filepath)+self.filepath.rfind('/')+1:-len(self.filepath)+self.filepath.find('.')]
    def dirpath(self):
        return self.filepath[:-len(self.filepath)+self.filepath.rfind('/')+1]

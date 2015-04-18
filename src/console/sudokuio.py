class SudokuIO(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.WRITE_MODE = 'r+'

    def write(self, text):
        file = open(self.file_path, self.WRITE_MODE)
        file.write(text)
        file.close()

    def read_all(self):
        print("Path: "+self.file_path)
        file = open(self.file_path)
        result = file.read()
        file.close()
        return result
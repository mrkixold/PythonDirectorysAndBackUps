import os

class Directory: 
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)
    def GetFileType(self, file):
        filetype = file.split('.')[-1]
        return filetype

    def RenameAllFiles(self, newname):
        counter = 0
        if(len(self.files)):
            for file in self.files:
                filetype = self.GetFileType(file)
                os.rename(self.path + '/' + file, self.path + '/' + newname + "_" + str(counter) + '.' + filetype)
                print("Renaming " + file + " to " + newname + "_" + str(counter) + "." + filetype)
                counter+=1
        else:
            print("Directory is empty")
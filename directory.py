import os

class Directory: 
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)
    def GetExtension(self, file):
        extension = file.split('.')[-1]
        return extension
    def GetFileType(self, file):
        filepath = self.path + '\\' + file
        filetype = ""
        if(os.path.isdir(filepath)):
            filetype = "folder"
            return filetype
        if(os.path.isfile(filepath)):
            filetype = "file"
            return filetype
        return "unknown"
    def RenameChildElement(self, file, newname):
        filetype = self.GetFileType(file)
        if(filetype == "folder"):
            os.rename(self.path + '/' + file, self.path + '/' + newname)
            print("Renaming " + file + " to " + newname)
        if(filetype == "file"):
            extension = ""
            if("." in file):
                extension = "." + self.GetExtension(file)
            os.rename(self.path + '/' + file, self.path + '/' + newname + extension)
            print("Renaming " + file + " to " + newname + extension)
    def RenameAllFiles(self, newname):
        counter = 1
        if(len(self.files)):
            for file in self.files:
                filename = newname + "_" + str(counter)
                self.RenameChildElement(file, filename)
                counter+=1
        else:
            print("Directory is empty")

    def RenameOnlyDivs(self, newname):
        counter = 1
        if(len(self.files)):
            for file in self.files: 
                filetype = self.GetFileType(file)
                if (filetype == "file"):
                    continue
                if(filetype=="folder"):
                    filename = newname + "_" + str(counter)
                    self.RenameChildElement(file, filename)
                    counter+=1
        else:
            print("Directory empty")

    def RenameOnlyFiles(self, newname):
        counter = 1
        if(len(self.files)):
            for file in self.files: 
                filetype = self.GetFileType(file)
                if (filetype == "folder"):
                    continue
                if(filetype=="file"):
                    filename = newname + "_" + str(counter)
                    self.RenameChildElement(file, filename)
                    counter+=1
        else:
            print("Directory empty")
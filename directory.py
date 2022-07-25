import os

class Directory: 
    def __init__(self, path):
        self.path = path
    
    files = os.listdir(path)
    
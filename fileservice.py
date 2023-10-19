#dont uppercase parameters
#comparing things to empty strings (a string with no value, blank) is something you'll do a lot

import time 

class FileService:
    def __init__(self, filename):
        self.filename = filename
        fl = open(filename, "a")
        fl.close()
        data = self.Load()
        if data == "":
            localtime = time.localtime()
            currenttime = time.strftime("%H:%M:%S", localtime)
            self.Save("lastlogin: " + currenttime)
            print("Created a new save file.")
        else: 
            print("A save file already exists.")
            print(data)

    def Save(self, data):
        fl = open(self.filename, "w")
        fl.write(data)

    def Load(self): 
        fl = open(self.filename, "r")
        data = fl.read()
        return data 

#FileService should have functions for reading, writing, creating files --  or maybe it should just have save and load,
# and that hides the low level stuff

#We're just saving and loading our player object. Should probably use JSON
#We might need to create a new save class instead of saving our player class directly (model)

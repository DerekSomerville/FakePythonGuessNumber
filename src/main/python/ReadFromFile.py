class ReadFromFile:

    def read(self, fileName):
        filePath = "src/main/resources/" + fileName
        openFile = open(filePath,"r")
        fileData = openFile.read().splitlines()
        openFile.close()
        return fileData

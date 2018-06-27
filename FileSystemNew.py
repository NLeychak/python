class FS:
    def __init__(self, name, subFile=None):
        self.name = name
        self.parent = None
        self.subFile = set()
        self.str = ""
        
    def addChild(self, subFile):
        self.subFile.add(subFile)
        subFile.parent = self
        
    def printPath(self, obj=None):
        return self.getPath(self)
        
    def getPath(self, obj):
        if obj.parent != None:
            return self.getPath(obj.parent) + '\\' + obj.name
        else:
            return '\\' + obj.name
            
    def printSubFiles(self):
        self.str = ', '.join(str(s.name) for s in self.subFile)
        return self.str
        
dir1 = FS("root")
dir2 = FS("main")
dir3 = FS("user")
fil1 = FS("my.txt")
fil2 = FS("old.ini")

dir1.addChild(dir2)
dir1.addChild(dir3)
dir3.addChild(fil1)
dir3.addChild(fil2)

dir3Path = dir3.printPath()
fil2Path = fil2.printPath()

dir3tSubFiles = dir3.printSubFiles()
dir3PathWithtSubFiles = dir3Path + '\\' + dir3tSubFiles

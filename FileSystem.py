class mLists:
    def __init__(self, string):
        self.mlist = list(string)

    def printList(self):
        unicList = self.delDbl(self.mlist)
        print(unicList)
        
    def delDbl(self, nonunicList):
        i = 0
        for x in nonunicList:
            count = nonunicList.count(x)
            if count >1:
                del nonunicList[i]
            i = i+1
        return nonunicList

mList = mLists("123454321 natasha")
mList.printList()
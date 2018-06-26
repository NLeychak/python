class mLists:
    def __init__(self, string):
        self.mlist = list(string)
        self.unicList = self.delDbl(self.mlist)
        
    def printList(self):
        print(self.unicList)
        
    def delDbl(self, nonunicList):
        i = 0
        for x in nonunicList:
            if nonunicList.count(x) >1:
                del nonunicList[i]
            i = i+1
        return nonunicList

mList = mLists("123454321 natasha")
mList.printList()

def ordered_set(inlist):
    out_list = []
    for val in inlist:
        if not val in out_list:
            out_list.append(val)
    return out_list
	
def make_unique(original_list):
    unique_list = []
    map(lambda x: unique_list.append(x) if (x not in unique_list) else False, original_list)
    return unique_list
	
data=[1, 2, 3, 1, 2, 5, 6, 7, 8]
uni_data=[]

for dat in data:
    if dat not in uni_data:
        uni_data.append(dat)

print(uni_data)
import random;
class ExtList:
    #myList = ExtList(6)
    #myList.fillList()
    #myList.printList()
    def __init__(self, size):
        self.lenght = size
        self.moutList = []
        
    def fillList(self):
        types = ['int', 'float', 'str']
        for i in range(0, self.lenght):
            j = random.choice(types)
            if j == 'int': item = random.randint(0, 100)
            elif j == 'float': item = round(random.uniform(0, 100), 3)
            else:
                item = ''
                for x in range(0, random.randint(0, 8)):
                    chr_val = random.randint(97, 122)
                    item = item + chr(chr_val)
            self.moutList.append(item)
        return self.moutList
            
    def printList(self):
        print self.moutList

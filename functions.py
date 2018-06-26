from ExtList import *

myList = ExtList(6)
myList = myList.fillList()
print 'Generated list:',myList
#myList = [82.482, 'ag', 49.118, 48.289, 6, 'itpdet', 10, '10']
d = None
VAT = 3.0
aa = 100
ba = 300

def int_or_float(inst):
    if isinstance(inst, int) or isinstance(inst, float):
        return True
    else: return False

def even_prnt(List):
    '''
    This is function!
    '''
    for i in List:
        if type(i) == int:
            if i%2 == 0: print i
            
even_prnt(myList)

def calc(a, b):
    if (int_or_float(a) and int_or_float(b)) or (isinstance(a, str) and isinstance(b, str)):
        a + b
    else: pass
    return a + b
print 'Calculator_summ\nA(',aa,') + B(',ba,') =', calc(aa, ba)

def VAT_price_calculator(price):
    summ = 0
    if int_or_float(price):
        summ = price + (price * (VAT / 100))
    return summ

print 'TAX = >', VAT_price_calculator(155)
#bar(3, 6, 7, 3)
    


a = 3
b = 'test'
c = [1, 2, 3]
d = 'none'
e = None
f = 0
list1 = ['hkvjxxzh', 71, 56, 39, 'e', 93, None, 5]
list2 = [16.995, 11.896, '', 76.159, 20, 'dzd', 71.323]

print 'a or b = >', a or b
print 'a and b = >', a and b
print 'a and d = >', a and d
print 'b or d = >', b or d
print 'a or f = >', a or f
print '##########################################'
print list1
for i in list1:
    if isinstance(i, int) or isinstance(i, float):
        if i > 5:
            print 'Yes   i > 5', i
        elif i < 5:
            print 'No   i < 5', i
        else: print 'Other i == 5 ', i
    elif type(i) == str:
        print 'string', i
    else:
        print 'other', i
        
print '##########################################'

print list1
for i in range(len(list1)):
    print 'in range = > ', list1[i]

for ii, j in enumerate(list1):
    print 'enumerate =>', ii, j

for i,j in zip(list1, list2):
    print 'ZIP => ', i, j
print '##########################################'
#Other

i = 5
exp = [20, 24, 36]
while i <= 47:
    if i not in exp:
        if i%2 == 0:
            print i
    i = i+1
print '##########################################'    

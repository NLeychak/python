def create_generator():
    for i in range(5):
        #print 'before yield'
        yield i * i
        #print 'after yield'

my_gen = create_generator()
for j in my_gen:
    print 'current j', j
    if j == 4:
        continue
else: print 'all iteration are done'
x = ''
try:
    x = input('Please enter: ')
except Exception:
    x = str(x)    
print 'input', x, 'type', type(x)

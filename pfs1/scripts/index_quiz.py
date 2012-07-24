N = int(raw_input('Enter a list size: '))
x = range(N)

print 'List:',              x
print 'Reversed:',          x[::-1]
print 'First six:',         x[:6]
print 'Last three:',        x[-3:]
print 'Minus last three:',  x[:-3]
print 'Middle minus 4:',    x[4:-4:3]
print 'First half:',        x[:len(x)/2]
print 'Last five, rev:',    x[:-6:-1]

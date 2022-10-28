f = open('f.txt', 'r')
g = open('g.txt', 'w')
s = ''
for c in f:
    s += c
f.close()
g.write(s[::-1])
g.close()
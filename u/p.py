import os 
f = open('saa', 'rb')
f = f.read()


f2 = open('i.jpg', 'wb')
f2.write(f)
f = open('paa', 'rb')
f = f.read()
f2.write(f)
f = open('sac', 'rb')
f = f.read()

f = open('saa', 'r')
f = f.read()
for i in f:
    print(i)


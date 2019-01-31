import os
import sys
f = open('img.jpg', 'rb')
f = f.read()
print(f[1:2])
f1 = open('f1.piece', 'wb')
f1.write(f)


















# for p in f:
#   print(hex(p), bin(p), type(p))






# f2 = open('f2.jpg', 'wb')

# for p in f:
#     f2.write(bytes(bin(p)))
    




# f2.write(f)

# for i in range(0, len(f)):
#     f2.write(f[i])
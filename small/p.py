import os
f = open('img.jpg', 'rb')
f = f.read()
f[4:8] = bytes('\xd8\xff\xe0\x00\x10JFIF')
f2 = open('f2.jpg', 'wb')
f2.write(f)

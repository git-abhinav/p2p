import socket                   
port = 50000                    
s = socket.socket()             
host = "192.168.0.4"   
s.bind((host, port))            
s.listen(5)                     
print ('S')
while True:
    conn, addr = s.accept()     
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    filename='i.jpg' 
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    print('Done sending')
    conn.send('Thanks')
    conn.close()
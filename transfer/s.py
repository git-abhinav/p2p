import socket # for connection 
import sys    # for commands 
def createSocket():
    global host
    global port 
    global s
    host = ""
    port = 9999
    try:
        s = socket.socket()
    except socket.error as message:
        print("Error while creating socket"+str(message))

# binding the socket and listening for connections 
def bindSocket():
    global host # accessing the global varibles of another function(createSocket)
    global port 
    global s
    print("Binding the port : "+str(port))
    try:
        s.bind((host,  port ))
        s.listen(5) # listen for connections
                    # 5 indicates max connection s
                    # it can tollerate 
    except socket.error as message:
        print("Error while creating socket "+str(message)+" trying again")
        bindSocket()

# establish connection with the client, socket must be listening 
def socketAccept():
    conn, address = s.accep()
    # for accepting the connection 
    # and it also gives two things in return 
    # 1. object of connection 
    # 2. list ip and and port 
    print("Connetion successful!", address)
    conn.close() # for closing the connection





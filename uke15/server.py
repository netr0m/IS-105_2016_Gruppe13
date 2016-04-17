# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Imports necessary modules  
import socket
import sys

# Unspecific host, meaning all available interfaces 
HOST = ''
# Set a port to use
PORT = 5000
 
# Create a datagram UDP socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "Socket has been created"
except socket.error, objct :
    print "An error has occured: Failed to create socket. Error Code : " + str(objct[0]) + " Message " + objct[1]
    sys.exit()
 
 
# Binds socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , objct:
    print "An error has occured: Bind failed. Error Code : " + str(objct[0]) + " Message " + objct[1]
    sys.exit()
     
print "Socket bind complete"
 
while 1:
    # Receive data from the client
    d = s.recvfrom(1024)
    # Data that the client sent (the object)
    data = d[0]
    # The address
    addr = d[1]
    
    # If there is no data 
    if not data: 
        break
    
    # Set the initial state of the world
    # "left", "boatLeft", "boatRight", "right":
    boat = "left"
    chicken = "left"
    grain = "left"
    fox = "left"
    
    # If data == an object going into the boat
    if data == "chickenIn" and chicken == "left":
        data = "chicken"
        chicken = "boatLeft"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
        
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    elif data == "chickenIn" and chicken == "right":
        data = "chicken"
        chicken = "boatLeft"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
        
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    elif data == "grainIn":
        data = "grain"
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() 
        
    elif data == "foxIn":
        data = "fox"
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n"
    
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
    
    elif data == "chickenOut":
        data = "chicken"
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()  
        
    elif data == "grainOut":
        data = "grain"
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()      
        
    elif data == "foxOut":
        data = "fox"
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()     
        
    elif data == "row":
        # The reply that the user will receive after sending a request/package 
        reply = "You have rowed to the other side of the river\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    elif data == "row":
        # The reply that the user will receive after sending a request/package 
        reply = "Current state of the River Crossing World:\n" + " hello\n"
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP         
        print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()    
s.close()        
        
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
    boatIsAt = "left"
    chickenIsAt = "left"
    grainIsAt = "left"
    foxIsAt = "left"
    
    # If data == "chickenIn", AND chicken is on the dock on the left side:
    if data == "chickenIn" and chickenIsAt == "left":
        data = "chicken"
        chickenIsAt = "boatLeft"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
        
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
    
    # If data == "chickenIn", AND chicken is on the dock on the right side:    
    elif data == "chickenIn" and chickenIsAt == "right":
        data = "chicken"
        chickenIsAt = "boatRight"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"
        
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
    
    # If data == "grainIn", AND grain is on the dock on the left side:    
    elif data == "grainIn" and grainIsAt == "left":
        data = "grain"
        grainIsAt = "boatLeft"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
    
    # If data == "grainIn", AND grain is on the dock on the right side:    
    elif data == "grainIn" and grainIsAt == "right":
        data = "grain"
        grainIsAt = "boatRight"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"
        
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()    

    # If data == "foxIn", AND fox is on the dock on the left side:    
    elif data == "foxIn" and foxIsAt == "left":
        data = "fox"
        foxIsAt = "boatLeft"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
    
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

    # If data == "foxIn", AND fox is on the dock on the right side:        
    elif data == "foxIn" and foxIsAt == "right":
        data = "fox"
        foxIsAt = "boatRight"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"
    
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
    
    # If data == "chickenOut", AND chicken is in the boat on the left side:    
    elif data == "chickenOut" and chickenIsAt == "boatLeft":
        data = "chicken"
        chickenIsAt = "left"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()  
    
    # If data == "chickenOut", AND chicken is in the boat on the right side:    
    elif data == "chickenOut" and chickenIsAt == "boatRight":
        data = "chicken"
        chickenIsAt = "right"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    elif data == "grainOut" and grainIsAt == "boatLeft":
        data = "grain"
        grainIsAt = "left"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    elif data == "grainOut" and grainIsAt == "boatRight":
        data = "grain"
        grainIsAt = "right"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()    
        
    elif data == "foxOut" and foxIsAt == "boatLeft":
        data = "fox"
        foxIsAt = "left"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()     
    
    elif data == "foxOut" and foxIsAt == "boatRight":
        data = "fox"
        foxIsAt = "right"
        
        # The reply that the user will receive after sending a request/package 
        reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()    
        
    elif data == "row":
        if boatIsAt == "left":
            boatIsAt = "right"
            # The reply that the user will receive after sending a request/package 
            reply = "You have rowed to the " + boatIsAt + " side of the river\n" + "The boat is on the " + boatIsAt + " side of the river\n"
        elif boatIsAt == "right":
            boatIsAt = "left"
            # The reply that the user will receive after sending a request/package
            reply = "You have rowed to the " + boatIsAt + " side of the river\n" + "The boat is on the " + boatIsAt + " side of the river\n"
            
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP
        print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()  
        
    elif data == "state" and boatIsAt == "left" and chicken == "left":
        # The reply that the user will receive after sending a request/package 
        reply = "Current state of the River Crossing World:\n" + " hello\n"
        # Send the reply to the client    
        s.sendto(reply, addr)
        # Print what object the client selected, and from which IP         
        print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()    
s.close()        
        
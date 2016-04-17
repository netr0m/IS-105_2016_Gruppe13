# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Imports necessary modules 
import socket
import sys

# Creates a datagram UDP socket 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# If an error occurs while attempting to create;
except socket.error:
    # Print an error message
    print "An error has occured: Failed to create socket"
    sys.exit()

# Set server "IP"/host 
host = 'localhost';
# Set port to use
port = 5000;
 
while(1) :
    userchoice = raw_input("""Select one of the following options to begin:
    R. Row to the other side
    Q. Put the chicken in the boat
    W. Put the chicken on the dock
    A. Put the grain in the boat
    S. Put the grain on the dock
    Z. Put the fox in the boat
    X. Put the fox on the dock
    E. See current state of the world\n
    """)
    userchoice = userchoice.upper()
    
    if userchoice == "Q":
        objct = "Q"
        try :
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
        
            # Prints the servers reply 
            print "Server reply:\n" + reply
    
        # If an error occurs; 
        except socket.error, objct:
            print "An error has occured: Error Code : " + str(objct[0]) + " Message " + objct[1]
            sys.exit()
    
    elif userchoice == "W":
        objct = "W"
        try :
            # Send the whole string
            s.sendto(objct, (host, port))
             
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply 
            print "Server reply: " + reply
        
        # If an error occurs; 
        except socket.error, objct:
            print "An error has occured: Error Code : " + str(objct[0]) + " Message " + objct[1]
            sys.exit()    
    
    elif userchoice == "A":
        objct = "A"
        try :
            # Send the whole string
            s.sendto(objct, (host, port))
             
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply 
            print "Server reply: " + reply
        
        # If an error occurs; 
        except socket.error, objct:
            print "An error has occured: Error Code : " + str(objct[0]) + " Message " + objct[1]
            sys.exit()
            
    elif userchoice == "S":
        objct = "S"
        try:
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply
            print "Server reply: " + reply
        # If an error occurs;
        except socket.error, objct:
            print "An error has occured: Error Code: " + str(objct[0]) + " Message " + objct[1]
            
    elif userchoice == "Z":
        objct = "Z"
        try:
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply
            print "Server reply: " + reply
        # If an error occurs;
        except socket.error, objct:
            print "An error has occured: Error Code: " + str(objct[0]) + " Message " + objct[1]
            
    elif userchoice == "X":
        objct = "X"
        try:
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply
            print "Server reply: " + reply
        # If an error occurs;
        except socket.error, objct:
            print "An error has occured: Error Code: " + str(objct[0]) + " Message " + objct[1]
            
    elif userchoice == "E":
        objct = "E"
        try:
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply
            print "Server reply: " + reply
        # If an error occurs;
        except socket.error, objct:
            print "An error has occured: Error Code: " + str(objct[0]) + " Message " + objct[1]
            
    elif userchoice == "R":
        objct = "R"
        try:
            # Send the whole string
            s.sendto(objct, (host, port))
            
            # Receive data from the server
            d = s.recvfrom(1024)
            # The reply that the server sent
            reply = d[0]
            # The address
            addr = d[1]
            
            # Prints the servers reply
            print "Server reply: " + reply
        # If an error occurs;
        except socket.error, objct:
            print "An error has occured: Error Code: " + str(objct[0]) + " Message " + objct[1]    
        
    else:
        print "Invalid choice."
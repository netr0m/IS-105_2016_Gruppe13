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
    userchoice = int(raw_input("""Select one of the following options to begin:
    1. Put an object in the boat
    2. Put an object on the dock
    3. Row to the other side
    4. See current state of the world\n"""))
    
    if userchoice == 1:
        objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put in the boat: ")
        objct = objct.lower()
        if objct == "chicken":
            objct = "chickenIn"
        elif objct == "grain":
            objct = "grainIn"
        elif objct == "fox":
            objct = "foxIn"
        else:
            print "There is no such object"
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
    
    elif userchoice == 2:
        objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put on the dock: ")
        objct = objct.lower()
        if objct == "chicken":
            objct = "chickenOut"
        elif objct == "grain":
            objct = "grainOut"
        elif objct == "fox":
            objct = "foxOut"
        else:
            print "There is no such object"

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
    
    elif userchoice == 3:
        objct = "row"
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
            
    elif userchoice == 4:
        objct = "state"
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
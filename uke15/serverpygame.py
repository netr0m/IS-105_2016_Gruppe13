# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Imports necessary modules  
import socket
import sys

# Unspecific host, meaning all available interfaces 
HOST = ''
# Set a port to use
PORT = 5000

# The initial state of the world
# Farmer X and Y values
fax = 260
fay = 580    
faxchange = 0

# Chicken X and Y values
cx = 30
cy = 525
cxchange = 0

# Grain X and Y values
gx = 90
gy = 570
gxchange = 0

# Fox X and Y values
fox = 145 
foy = 575
foxchange = 0 

# Boat X and Y values
bx = 255
by = 620
bchange = 0

victory = False
finished = False

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
    # Data that the client sent (new x values)
    dataX = d[2]
    # Data that the client sent (new y values)
    dataY = d[3]
    # The address
    addr = d[1]

    # If there is no data 
    if not data: 
        break

    # If data == "Q" (put chicken in boat);
    if data == "Q":
        # If chicken is on the dock on the left side:
        if cx == 30:
            data = "chicken"
            cx = cx
            cy = cy
            print "CX: " + cx
            print "CY: " + cy

            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + chickenIsAt

        # If chicken is on the dock on the right side:    
        elif cx == 1210:
            data = "chicken"
            cx = cx
            cy = cy
            print "CX: " + cx
            print "CY: " + cy            
            
            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + chickenIsAt

    # If data == "A" (put grain in boat):
    elif data == "A":
        # If grain is on the dock on the left side:
        if grainIsAt == "left":
            data = "grain"
            grainIsAt = "boatLeft"
            
            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + grainIsAt

        # If grain is on the dock on the right side:    
        elif grainIsAt == "right":
            data = "grain"
            grainIsAt = "boatRight"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + grainIsAt  

    # If data == "Z" (put fox in boat):    
    elif data == "Z":
        # If fox is on the dock on the left side:
        if foxIsAt == "left":
            data = "fox"
            foxIsAt = "boatLeft"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + foxIsAt

        # If fox is on the dock on the right side:        
        elif foxIsAt == "right":
            data = "fox"
            foxIsAt = "boatRight"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the right side\n"

            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + foxIsAt

    # If data == "W" (put chicken on dock):    
    elif data == "W":
        # If chicken is in the boat on the left side:
        if chickenIsAt == "boatLeft":
            data = "chicken"
            chickenIsAt = "left"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"

            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + chickenIsAt

        # If chicken is in the boat on the right side:    
        elif chickenIsAt == "boatRight":
            data = "chicken"
            chickenIsAt = "right"
            
            # If the chicken, the grain and the fox are on the right:
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                reply = "You won the game! Congratulations\nRestarting the game.\n"
                # Send the reply to the client
                s.sendto(reply, addr)
                # Print what outcome occured
                print 'The client won the game! (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            else:            
                # The reply that the user will receive after sending a request/package 
                reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what object the client selected, and from which IP
                print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + chickenIsAt            

    # If data == "S" (put grain on dock):   
    elif data == "S":
        # If grain is in the boat on the left side: 
        if grainIsAt == "boatLeft":
            data = "grain"
            grainIsAt = "left"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"

            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + grainIsAt

        # If grain is in the boat on the right side:    
        elif grainIsAt == "boatRight":
            data = "grain"
            grainIsAt = "right"
            
            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + grainIsAt   

    # If data == "X" (put fox on dock):    
    elif data == "X":
        # If fox is in the boat on the left side:
        if foxIsAt == "boatLeft":
            data = "fox"
            foxIsAt = "left"

            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the left dock\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + foxIsAt

        # If fox is in the boat on the right side:
        elif foxIsAt == "boatRight":
            data = "fox"
            foxIsAt = "right"
            
            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " on the dock.\n" + "The " + data + " is on the right dock\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + foxIsAt

    # If data == "R" (Row to the other side):
    elif data == "R":
        # If boat is on the left side:
        if boatIsAt == "left":
            data = "Row"
            boatIsAt = "right"
            
            # If the chicken is alone with the grain:
            if chickenIsAt == "left" and grainIsAt == "left" and foxIsAt != "left":
                reply = "You lost the game..\nThe chicken ate the grain.\nRestarting the game.\n"
                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what outcome occured
                print 'Game over.. Chicken ate the grain (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            # If the fox is alone with the chicken:    
            elif chickenIsAt == "left" and foxIsAt == "left":
                reply = "You lost the game..\nThe fox ate the chicken.\nRestarting the game.\n"
                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what outcome occured
                print 'Game over.. Fox ate the chicken (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
                
            # If the chicken, the grain and the fox are on the right:
            elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                reply = "You won the game! Congratulations\nRestarting the game.\n"
                # Send the reply to the client
                s.sendto(reply, addr)
                # Print what outcome occured
                print 'The client won the game! (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            # If chicken is in the boat, on the left side:
            elif chickenIsAt == "boatLeft":
                # Move to the right side
                chickenIsAt = "boatRight"
                # Print that the chicken has moved
                print "The chicken is now in the boat on the right side"
                # Define that it's in the boat:
                inBoat = "chicken"
            # If grain is in the boat, on the left side:
            elif grainIsAt == "boatLeft":
                # Move to the right side                
                grainIsAt = "boatRight"
                # Print that the grain has moved
                print "The grain is now in the boat on the right side"
                # Define that it's in the boat:
                inBoat = "grain"
            # If fox is in the boat, on the left side:
            elif foxIsAt == "boatLeft":
                # Move to the right side
                foxIsAt = "boatRight"
                # Print that the fox has moved
                print "The fox is now in the boat on the right side"
                # Define that it's in the boat:
                inBoat = "fox"
            
            else:
                inBoat = "empty"
                if inBoat == "empty":
                    reply = "You lost the game.. The fox ate the chicken.\n Restarting the game.\n"
                    # Send the reply to the client    
                    s.sendto(reply, addr)
                    # Print what outcome occured
                    print 'Game over.. Fox ate the chicken(from [' + addr[0] + ':' + str(addr[1]) + '])'
                    execfile("server.py")

            # The reply that the user will receive after sending a request/package
            reply = "You have rowed to the " + boatIsAt + " side of the river with the " + inBoat + "\n" + "The boat is on the " + boatIsAt + " side of the river\n"

            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + " " + boatIsAt + " with " + inBoat

        # If boat is on the right side:    
        elif boatIsAt == "right":
            data = "Row"
            boatIsAt = "left"
            
            # If the chicken is alone with the grain:    
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt != "right":
                reply = "You lost the game..\nThe chicken ate the grain.\nRestarting the game.\n"
                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what outcome occured
                print 'Game over.. Chicken ate the grain (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            # If the fox is alone with the chicken:    
            elif chickenIsAt == "right" and foxIsAt == "right":
                reply = "You lost the game..\nThe fox ate the chicken.\nRestarting the game.\n"
                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what object the client selected, and from which IP
                print 'Game over.. Fox ate the chicken (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")

            # If chicken is in the boat, on the left side:
            elif chickenIsAt == "boatRight":
                # Move to the left side
                chickenIsAt = "boatLeft"
                # Print that the chicken has moved
                print "The chicken is now in the boat on the left side"
                # Define that it's in the boat:
                inBoat = "chicken"
            # If grain is in the boat, on the left side:
            elif grainIsAt == "boatRight":
                # Move to the right side                
                grainIsAt = "boatLeft"
                # Print that the grain has moved
                print "The grain is now in the boat on the left side"
                # Define that it's in the boat:
                inBoat = "grain"
            # If fox is in the boat, on the left side:
            elif foxIsAt == "boatRight":
                # Move to the right side
                foxIsAt = "boatLeft"
                # Print that the fox has moved
                print "The fox is now in the boat on the left side"
                # Define that it's in the boat:
                inBoat = "fox"          

            # The reply that the user will receive after sending a request/package 
            if chickenIsAt == "boatLeft" or chickenIsAt == "boatRight" or grainIsAt == "boatLeft" or grainIsAt == "boatRight" or foxIsAt == "boatLeft" or foxIsAt == "boatLeft":
                reply = "You have rowed to the " + boatIsAt + " side of the river with the " + inBoat + "\n" + "The boat is on the " + boatIsAt + " side of the river\n"
            else:
                reply = "You have rowed to the " + boatIsAt + " side of the river.\n" + "The boat is on the " + boatIsAt + " side of the river\n"

            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            if chickenIsAt == "boatLeft" or chickenIsAt == "boatRight" or grainIsAt == "boatLeft" or grainIsAt == "boatRight" or foxIsAt == "boatLeft" or foxIsAt == "boatLeft":
                print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + " " + boatIsAt + " with " + inBoat
            else:
                print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + " " + boatIsAt
s.close()        

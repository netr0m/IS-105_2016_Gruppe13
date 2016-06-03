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
            if not gx == 400 or fox == 400:
                cx += 370
                cy += 75

                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

        # If chicken is on the dock on the right side:    
        elif cx == 1210:
            data = "chicken"
            if not gx == 965 or fox == 965:
                cx -= 245
                cy += 75
    
                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

    # If data == "A" (put grain in boat):
    elif data == "A":
        # If grain is on the dock on the left side:
        if gx == 90:
            data = "grain"
            if not cx == 400 or fox == 400:
                gx +=310
                gy +=30
                
                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
            
        # If grain is on the dock on the right side:
        elif gx == 1170:
            data = "grain"
            if not cx == 965 or fox == 965:
                gx -=205
                gy += 30
                
                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()                

    # If data == "Z" (put fox in boat):    
    elif data == "Z":
        # If fox is on the dock on the left side:
        if fox == 145:
            data = "fox"
            if not cx == 400 or gx == 400:
                fox += 255
                foy += 15
    
                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

        # If fox is on the dock on the right side:        
        elif fox == 1120:
            data = "fox"
            if not cx == 965 or fox == 965:
                fox -= 155
                foy += 15
                
                # Print what object the client selected, and from which IP
                print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

    # If data == "W" (put chicken on dock):    
    elif data == "W":
        # If chicken is in the boat on the left side:
        if cx == 400:
            data = "chicken"
            cx -= 370
            cy -= 75

            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

        # If chicken is in the boat on the right side:    
        elif cx == 965:
            data = "chicken"
            cx += 245
            cy -= 75
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
            
        else:
            pass

    # If data == "S" (put grain on dock):   
    elif data == "S":
        # If grain is in the boat on the left side: 
        if gx == 400:
            data = "grain"
            gx -= 310
            gy -= 30
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

        # If grain is in the boat on the right side:    
        elif gx == 965:
            data = "grain"
            gx += 205
            gy -= 30
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()   

    # If data == "X" (put fox on dock):    
    elif data == "X":
        # If fox is in the boat on the left side:
        if fox == 400:
            data = "fox"
            fox -= 255
            foy -= 15
            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

        # If fox is in the boat on the right side:
        elif fox == 965:
            data = "fox"
            fox += 155
            foy += 15

            # Print what object the client selected, and from which IP
            print 'Object put on dock (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()

    # If data == "R" (Row to the other side):
    elif data == "R":
        # If boat is on the left side:
        if bx == 255:
            data = "Row"
            if cx == 400:
                cx += 565
            elif gx == 400:
                gx += 565
            elif fox == 400:
                fox += 565
            fax += 565
            bx += 565
        elif bx == 820:
            if cx == 965:
                cx -= 565
            elif gx == 965:
                gx -= 565
            elif fox == 965:
                fox -= 565
            fax -= 565
            bx -= 565
        else:
            pass

        # Print what object the client selected, and from which IP
        print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip()
        
    def forbidden(x):
        if x == 1:
            print 'The wolf ate the chicken. Game lost, Restarting.. (from [' + addr[0] + ':' + str(addr[1]) + ']): '
            s.close()
            execfile("server.py")
        elif x == 2:
            print 'The wolf ate the chicken. Game lost, Restarting.. (from [' + addr[0] + ':' + str(addr[1]) + ']): '
            s.close()
            execfile("server.py")
        elif x == 3:
            print 'The chicken ate the grain. Game lost, Restarting..(from [' + addr[0] + ':' + str(addr[1]) + ']): '
            s.close()
            execfile("server.py")
            
    # Define what outcomes are forbidden:
    #  If bx (boat X-value) equals 820, cx (chicken X-value) equals 30, and fox (fox X-value) equals 145:
    # Display forbidden(1) message
    if bx == 820 and cx == 30 and fox == 145:
        forbidden(1)
    
    # Display forbidden(2) message    
    if bx == 255 and fox == 1120 and cx == 1210:
            forbidden(2)            
    
    # Display forbidden(3) message        
    if bx == 255 and cx == 1210 and gx == 1170:
                forbidden(3)
    
    # Display forbidden(3) message
    if bx == 820 and cx == 30 and gx == 90:
        forbidden(3)
    
    # If all objects are on the right bank/dock, set victory to true, player wins the game            
    if fox == 1120 and gx == 1170 and cx == 1210:
        victory = True
        
    if victory:
        print 'The client won the game! Restarting.. (from [' + addr[0] + ':' + str(addr[1]) + ']): '
        s.close()
        execfile("server.py")
s.close()

# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Imports necessary modules  
import socket
import sys

# Unspecific host, meaning all available interfaces 
HOST = ''
# Set a port to use
PORT = 5000

# Set the initial state of the world
# "left", "boatLeft", "boatRight", "right":
boatIsAt = "left"
chickenIsAt = "left"
grainIsAt = "left"
foxIsAt = "left"

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
        if chickenIsAt == "left":
            data = "chicken"
            chickenIsAt = "boatLeft"
            
            # The reply that the user will receive after sending a request/package 
            reply = "You put the " + data + " in the boat.\n" + "The " + data + " is in the boat on the left side\n"
            
            # Send the reply to the client    
            s.sendto(reply, addr)
            # Print what object the client selected, and from which IP
            print 'Object put in boat (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + ", " + chickenIsAt

        # If chicken is on the dock on the right side:    
        elif chickenIsAt == "right":
            data = "chicken"
            chickenIsAt = "boatRight"
            
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

    # If data == "E", show the current state of the world:    
    elif data == "E":
        if boatIsAt == "left":
            if chickenIsAt == "left" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply

            elif chickenIsAt == "boatLeft" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "right" and grainIsAt == "boatLeft" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif grainIsAt == "right" and chickenIsAt == "boatLeft" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
            
            elif foxIsAt == "boatLeft" and chickenIsAt == "left" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken grain \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
        if boatIsAt == "right":
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ /fox grain chicken]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "boatRight" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ /---]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "right" and grainIsAt == "boatRight" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply                
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply                
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / fox grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
            
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply  
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / fox ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply

            elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / grain chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply

            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / fox chicken ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply

            elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
                
            elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / fox grain ]\n"""

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Current state (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply
            
            else:
                # The reply that the user will receive after sending a request/package 
                reply = "Error. Game restarted"

                # Send the reply to the client    
                s.sendto(reply, addr)
                # Print what action the client performed, and from which IP         
                print 'Error occured (game over) (from [' + addr[0] + ':' + str(addr[1]) + ']):\n' + reply

s.close()        

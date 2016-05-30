# Set the initial state of the world
# "left", "boatLeft", "boatRight", "right":
boatIsAt = "left"
chickenIsAt = "left"
grainIsAt = "left"
foxIsAt = "left"

    # If data == "Q" (put chicken in boat);
    if data == "Q":
        # If chicken is on the dock on the left side:
        if chickenIsAt == "left":
            data = "chicken"
            chickenIsAt = "boatLeft"

        # If chicken is on the dock on the right side:    
        elif chickenIsAt == "right":
            data = "chicken"
            chickenIsAt = "boatRight"
            
    # If data == "A" (put grain in boat):
    elif data == "A":
        # If grain is on the dock on the left side:
        if grainIsAt == "left":
            data = "grain"
            grainIsAt = "boatLeft"

        # If grain is on the dock on the right side:    
        elif grainIsAt == "right":
            data = "grain"
            grainIsAt = "boatRight"

    # If data == "Z" (put fox in boat):    
    elif data == "Z":
        # If fox is on the dock on the left side:
        if foxIsAt == "left":
            data = "fox"
            foxIsAt = "boatLeft"

        # If fox is on the dock on the right side:        
        elif foxIsAt == "right":
            data = "fox"
            foxIsAt = "boatRight"

    # If data == "W" (put chicken on dock):    
    elif data == "W":
        # If chicken is in the boat on the left side:
        if chickenIsAt == "boatLeft":
            data = "chicken"
            chickenIsAt = "left"

        # If chicken is in the boat on the right side:    
        elif chickenIsAt == "boatRight":
            data = "chicken"
            chickenIsAt = "right"
            
            # If the chicken, the grain and the fox are on the right:
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                reply = "You won the game! Congratulations\nRestarting the game.\n"
                # Print what outcome occured
                print 'The client won the game! (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")

    # If data == "S" (put grain on dock):   
    elif data == "S":
        # If grain is in the boat on the left side: 
        if grainIsAt == "boatLeft":
            data = "grain"
            grainIsAt = "left"

        # If grain is in the boat on the right side:    
        elif grainIsAt == "boatRight":
            data = "grain"
            grainIsAt = "right"

    # If data == "X" (put fox on dock):    
    elif data == "X":
        # If fox is in the boat on the left side:
        if foxIsAt == "boatLeft":
            data = "fox"
            foxIsAt = "left"

        # If fox is in the boat on the right side:
        elif foxIsAt == "boatRight":
            data = "fox"
            foxIsAt = "right"

    # If data == "R" (Row to the other side):
    elif data == "R":
        # If boat is on the left side:
        if boatIsAt == "left":
            data = "Row"
            boatIsAt = "right"
            
            # If the chicken is alone with the grain:
            if chickenIsAt == "left" and grainIsAt == "left" and foxIsAt != "left":
                reply = "You lost the game..\nThe chicken ate the grain.\nRestarting the game.\n"
                # Print what outcome occured
                print 'Game over.. Chicken ate the grain (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            # If the fox is alone with the chicken:    
            elif chickenIsAt == "left" and foxIsAt == "left":
                reply = "You lost the game..\nThe fox ate the chicken.\nRestarting the game.\n"
                # Print what outcome occured
                print 'Game over.. Fox ate the chicken (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
                
            # If the chicken, the grain and the fox are on the right:
            elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                reply = "You won the game! Congratulations\nRestarting the game.\n"
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
                    # Print what outcome occured
                    print 'Game over.. Fox ate the chicken(from [' + addr[0] + ':' + str(addr[1]) + '])'
                    execfile("server.py")

            # The reply that the user will receive after sending a request/package
            reply = "You have rowed to the " + boatIsAt + " side of the river with the " + inBoat + "\n" + "The boat is on the " + boatIsAt + " side of the river\n"

            # Print what object the client selected, and from which IP
            print 'Action performed (from [' + addr[0] + ':' + str(addr[1]) + ']): ' + data.strip() + " " + boatIsAt + " with " + inBoat

        # If boat is on the right side:    
        elif boatIsAt == "right":
            data = "Row"
            boatIsAt = "left"
            
            # If the chicken is alone with the grain:    
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt != "right":
                reply = "You lost the game..\nThe chicken ate the grain.\nRestarting the game.\n"
                # Print what outcome occured
                print 'Game over.. Chicken ate the grain (from [' + addr[0] + ':' + str(addr[1]) + '])'
                execfile("server.py")
            
            # If the fox is alone with the chicken:    
            elif chickenIsAt == "right" and foxIsAt == "right":
                reply = "You lost the game..\nThe fox ate the chicken.\nRestarting the game.\n"
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

            elif chickenIsAt == "boatLeft" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            elif chickenIsAt == "right" and grainIsAt == "boatLeft" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            elif grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                
            elif grainIsAt == "right" and chickenIsAt == "boatLeft" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
            
            elif foxIsAt == "boatLeft" and chickenIsAt == "left" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken grain \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "boatLeft":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "boatLeft" and grainIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""
                
        if boatIsAt == "right":
            if chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ /fox grain chicken]\n"""
                
            elif chickenIsAt == "boatRight" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ /---]\n"""
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken ]\n"""
                
            elif chickenIsAt == "right" and grainIsAt == "boatRight" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken ]\n"""        
                
            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken ]\n"""          
                
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / fox grain ]\n"""
            
            elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / grain ]\n"""
                
            elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "boatRight":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / fox ]\n"""

            elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / grain chicken ]\n"""

            elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / fox chicken ]\n"""

            elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / grain ]\n"""
                
            elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "right":
                # The reply that the user will receive after sending a request/package 
                reply = """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / fox grain ]\n"""

s.close()        
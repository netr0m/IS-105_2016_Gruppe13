# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Set the initial state of the world
# "left", "boatLeft", "boatRight", "right":
boatIsAt = "left"
chickenIsAt = "left"
grainIsAt = "left"
foxIsAt = "left"

# Game won, or game over
gameEnd = False

print """\nCurrent state of the River Crossing World:
                [ chicken grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
while(gameEnd == False):
    # Make the user choose an action to perform
    userchoice = int(raw_input("""Select one of the following options to begin:
    1. Put an object in the boat
    2. Put an object on the dock
    3. Row to the other side\n"""))
    
    # 1, put something in the boat
    if userchoice == 1:
        # Select an object
        objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put in the boat: ")
        objct = objct.lower()
        
        # If the object chosen is chicken
        if objct == "chicken":
            if chickenIsAt == "left":
                if boatIsAt == "left":
                    chickenIsAt = "boatLeft"
                    if chickenIsAt == "boatLeft" and grainIsAt == "left" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ grain fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                        
                    elif chickenIsAt == "boatLeft" and grainIsAt == "right" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                        
                    elif chickenIsAt == "boatLeft" and grainIsAt == "left" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ grain \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                        
                    elif chickenIsAt == "boatLeft" and grainIsAt == "right" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [---\ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""
                        
                elif boatIsAt == "right":
                    print "The boat is on the other side."
                
            elif chickenIsAt == "right":
                if boatIsAt == "right":
                    chickenIsAt = "boatRight"
                    if chickenIsAt == "boatRight" and grainIsAt == "left" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ /---]\n"""
                        
                    elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / grain ]\n"""
                        
                    elif chickenIsAt == "boatRight" and grainIsAt == "left" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / fox ]\n"""
                        
                    elif chickenIsAt == "boatRight" and grainIsAt == "right" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / fox grain ]\n"""
                        
                elif boatIsAt == "right":
                    print "The boat is on the other side."
        
        # If the object chosen is grain
        elif objct == "grain":
            if grainIsAt == "left":
                if boatIsAt == "left":
                    grainIsAt = "boatLeft"
                    if grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                        
                    elif grainIsAt == "boatLeft" and chickenIsAt == "right" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                        
                    elif grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                        
                    else:
                        print "Game over! Restarting game..."
                        execfile("1.2.1d.py")
                        
                elif boatIsAt == "right":
                    print "The boat is on the other side."
                
                    
            elif grainIsAt == "right":
                if boatIsAt == "right":
                    grainIsAt = "boatRight"                    
                    if grainIsAt == "boatRight" and chickenIsAt == "right" and foxIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken ]\n"""
                        
                    elif grainIsAt == "boatRight" and chickenIsAt == "left" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / fox ]\n"""
                        
                    elif grainIsAt == "boatRight" and chickenIsAt == "right" and foxIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken fox ]\n"""
                        
                    else:
                        print "Game over! Restarting game..."
                        execfile("1.2.1d.py")                
                    
                elif boatIsAt == "right":
                    print "The boat is on the other side."                
                    
            
        # If the object chosen is fox
        elif objct == "fox":
            if foxIsAt == "left":
                if boatIsAt == "left":
                    foxIsAt = "boatLeft"
                    if foxIsAt == "boatLeft" and grainIsAt == "left" and chickenIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                        
                    elif foxIsAt == "boatLeft" and grainIsAt == "right" and chickenIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                        
                    elif foxIsAt == "boatLeft" and grainIsAt == "left" and chickenIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""             
                        
                    else:
                        print "Game over! Restarting game..."
                        execfile("1.2.1d.py")
                        
                elif boatIsAt == "right":
                    print "The boat is on the other side."                
                    
                
            elif foxIsAt == "right":
                if boatIsAt == "right":
                    foxIsAt = "boatRight"
                    if foxIsAt == "boatRight" and grainIsAt == "right" and chickenIsAt == "left":
                        print """\nCurrent state of the River Crossing World:
                        [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / grain ]\n"""
                        
                    elif foxIsAt == "boatRight" and grainIsAt == "left" and chickenIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken ]\n"""
                        
                    elif foxIsAt == "boatRight" and grainIsAt == "right" and chickenIsAt == "right":
                        print """\nCurrent state of the River Crossing World:
                        [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken grain ]\n"""
                        
                    else:
                        print "Game over! Restarting game..."
                        execfile("1.2.1d.py")
                        
                elif boatIsAt == "right":
                    print "The boat is on the other side."
                
        # Object chosen does not exist        
        else:
            print "There is no such object"
    
    elif userchoice == 2:
        objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put on the dock: ")
        objct = objct.lower()
        if objct == "chicken":
            if chickenIsAt == "boatLeft":
                chickenIsAt = "left"
                if chickenIsAt == "left" and grainIsAt == "left" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                    
                elif chickenIsAt == "left" and grainIsAt == "right" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                    
                elif chickenIsAt == "left" and grainIsAt == "left" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken grain \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                    
                elif chickenIsAt == "left" and grainIsAt == "right" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""
                
            elif chickenIsAt == "boatRight":
                chickenIsAt = "right"
                if chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken ]\n"""
                    
                elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken grain ]\n"""
                    
                elif chickenIsAt == "right" and grainIsAt == "left" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken fox ]\n"""
                    
                elif chickenIsAt == "right" and grainIsAt == "right" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken fox grain ]\n"""
                    print "You won the game! Congratulations.\nRestarting the game..."
                    execfile("1.2.1d.py")
            
        elif objct == "grain":
            if grainIsAt == "boatLeft":
                grainIsAt = "left"
                if grainIsAt == "left" and chickenIsAt == "left" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                    
                elif grainIsAt == "left" and chickenIsAt == "right" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                    
                elif grainIsAt == "left" and chickenIsAt == "left" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken grain \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                    
                else:
                    print "Game over! Restarting game..."
                    execfile("1.2.1d.py")
                
            elif grainIsAt == "boatRight":
                grainIsAt = "right"                    
                if grainIsAt == "right" and chickenIsAt == "right" and foxIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken grain ]\n"""
                    
                elif grainIsAt == "right" and chickenIsAt == "left" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / grain fox ]\n"""
                    
                elif grainIsAt == "right" and chickenIsAt == "right" and foxIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken fox grain ]\n"""
                    print "You won the game! Congratulations.\nRestarting the game..."
                    execfile("1.2.1d.py")
                    
                else:
                    print "Game over! Restarting game..."
                    execfile("1.2.1d.py")
    
        elif objct == "fox":
            if foxIsAt == "boatLeft":
                foxIsAt = "left"
                if foxIsAt == "left" and chickenIsAt == "left" and grainIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                    
                elif foxIsAt == "left" and chickenIsAt == "right" and grainIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                    
                elif foxIsAt == "left" and chickenIsAt == "left" and grainIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                    
                else:
                    print "Game over! Restarting game..."
                    execfile("1.2.1d.py")                
                
            elif foxIsAt == "boatRight":
                foxIsAt = "right"
                if foxIsAt == "right" and chickenIsAt == "right" and grainIsAt == "left":
                    print """\nCurrent state of the River Crossing World:
                    [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken fox ]\n"""
                    
                elif foxIsAt == "right" and chickenIsAt == "left" and grainIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / grain fox ]\n"""
                    
                elif foxIsAt == "right" and chickenIsAt == "right" and grainIsAt == "right":
                    print """\nCurrent state of the River Crossing World:
                    [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man _/ / chicken fox grain ]\n"""
                    print "You won the game! Congratulations.\nRestarting the game..."
                    execfile("1.2.1d.py")
                    
                else:
                    print "Game over! Restarting game..."
                    execfile("1.2.1d.py")                
    
        else:
            print "There is no such object"
    
    elif userchoice == 3:
        if boatIsAt == "left":
            boatIsAt = "right"
            
            # CHICKEN
            if chickenIsAt == "boatLeft" and foxIsAt == "left" and grainIsAt == "left":
                chickenIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ grain fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ /---]\n"""
                
            elif chickenIsAt == "boatLeft" and foxIsAt == "right" and grainIsAt == "left":
                chickenIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / fox ]\n"""
                
            elif chickenIsAt == "boatLeft" and foxIsAt == "left" and grainIsAt == "right":
                chickenIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / grain ]\n"""
                
            elif chickenIsAt == "boatLeft" and foxIsAt == "right" and grainIsAt == "right":
                chickenIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + chicken _/ / grain fox ]\n"""
                
            # FOX
            elif foxIsAt == "boatLeft" and chickenIsAt == "left" and grainIsAt == "left":
                foxIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ chicken grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ /---]\n"""
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")                
                
            elif foxIsAt == "boatLeft" and chickenIsAt == "right" and grainIsAt == "left":
                foxIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ grain \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken ]\n"""
                
            elif foxIsAt == "boatLeft" and chickenIsAt == "left" and grainIsAt == "right":
                foxIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / grain ]\n"""
                
            elif foxIsAt == "boatLeft" and chickenIsAt == "right" and grainIsAt == "right":
                foxIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + fox _/ / chicken grain ]\n"""

            # GRAIN
            elif grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "left":
                grainIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ chicken fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ /---]\n"""
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")                
                
            elif grainIsAt == "boatLeft" and chickenIsAt == "right" and foxIsAt == "left":
                grainIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ fox \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken ]\n"""
                
            elif grainIsAt == "boatLeft" and chickenIsAt == "left" and foxIsAt == "right":
                grainIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [ chicken \ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / fox ]\n"""
                
            elif grainIsAt == "boatLeft" and chickenIsAt == "right" and foxIsAt == "right":
                grainIsAt = "boatRight"
                print """\nCurrent state of the River Crossing World:
                [---\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \_ man + grain _/ / chicken fox ]\n"""
                
            else:
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")            

        elif boatIsAt == "right":
            boatIsAt = "left"
            
            # CHICKEN
            if chickenIsAt == "boatRight" and foxIsAt == "left" and grainIsAt == "left":
                chickenIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
                
            elif chickenIsAt == "boatRight" and foxIsAt == "right" and grainIsAt == "left":
                chickenIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif chickenIsAt == "boatRight" and foxIsAt == "left" and grainIsAt == "right":
                chickenIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                
            elif chickenIsAt == "boatRight" and foxIsAt == "right" and grainIsAt == "right":
                chickenIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [---\ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain fox ]\n"""
                
            elif chickenIsAt == "right" and foxIsAt == "left" and grainIsAt == "left":
                print """\nCurrent state of the River Crossing World:
                [ grain fox \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            # FOX                
            elif foxIsAt == "boatRight" and chickenIsAt == "right" and grainIsAt == "left":
                foxIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ grain \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            elif foxIsAt == "boatRight" and chickenIsAt == "left" and grainIsAt == "right":
                foxIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / grain ]\n"""
                
            elif foxIsAt == "boatRight" and chickenIsAt == "right" and grainIsAt == "right":
                foxIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [---\ \_ man + fox _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken grain ]\n"""
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")        

            # GRAIN
            elif grainIsAt == "boatRight" and chickenIsAt == "right" and foxIsAt == "left":
                grainIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ fox \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken ]\n"""
                
            elif grainIsAt == "boatRight" and chickenIsAt == "left" and foxIsAt == "right":
                grainIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox ]\n"""
                
            elif grainIsAt == "boatRight" and chickenIsAt == "right" and foxIsAt == "right":
                grainIsAt = "boatLeft"
                print """\nCurrent state of the River Crossing World:
                [---\ \_ man + grain _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / chicken fox ]\n"""
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")                   
                
            # EXTRA   
            elif chickenIsAt == "left" and grainIsAt == "right" and foxIsAt == "right":
                print """\nCurrent state of the River Crossing World:
                [ chicken \ \_ man _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ / fox grain ]\n"""                
                
            else:
                print "Game over! Restarting game..."
                execfile("1.2.1d.py")
        
    else:
        print "Invalid choice."
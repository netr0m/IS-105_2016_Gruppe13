# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Set the initial state of the world
# "left", "boatLeft", "boatRight", "right":
boatIsAt = "left"
chickenIsAt = "left"
grainIsAt = "left"
foxIsAt = "left"

# Make the user choose an action to perform
userchoice = int(raw_input("""Select one of the following options to begin:
1. Put an object in the boat
2. Put an object on the dock
3. Row to the other side"""))

# 1, put something in the boat
if userchoice == 1:
    # Select an object
    objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put in the boat: ")
    objct = objct.lower()
    
    # If the object chosen is a chicken
    if objct == "chicken":
        if chickenIsAt == "left":
            chickenIsAt = "boatLeft"
            if chickenIsAt == "boatLeft" and grainIsAt == "left" and foxIsAt == "left":
                # The reply that the user will receive after sending a request/package 
                print """\nCurrent state of the River Crossing World:
                        [ grain fox \ \_ man + chicken _/ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ /---]\n"""
            
        elif chickenIsAt == "right":
            chickenIsAt = "boatRight"
    
    # If the object chosen is grain
    elif objct == "grain":
        if grainIsAt == "left":
            grainIsAt = "boatLeft"
        elif grainIsAt == "right":
            grainIsAt = "boatRight"
        
    # If the object chosen is a fox
    elif objct == "fox":
        if foxIsAt == "left":
            foxIsAt = "boatLeft"
        elif foxIsAt == "right":
            foxIsAt = "boatRight"
            
    # Object chosen does not exist        
    else:
        print "There is no such object"

elif userchoice == 2:
    objct = raw_input("Type to select either 'Chicken', 'Grain', or 'Fox' to put on the dock: ")
    objct = objct.lower()
    if objct == "chicken":
        if chickenIsAt == "boatLeft":
            chickenIsAt = "left"
        elif chickenIsAt == "boatRight":
            chickenIsAt = "right"        
        
    elif objct == "grain":
        if grainIsAt == "boatLeft":
            grainIsAt = "left"
        elif grainIsAt == "boatRight":
            grainIsAt = "right"        

    elif objct == "fox":
        if foxIsAt == "boatLeft":
            foxIsAt = "left"
        elif foxIsAt == "boatRight":
            foxIsAt = "right"        

    else:
        print "There is no such object"

elif userchoice == 3:
    objct = "row"
    
else:
    print "Invalid choice."
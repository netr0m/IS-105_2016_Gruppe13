# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Louise Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
# Script for the river-cross-problem
# The chicken, fox and the grain should be transported from the left side to the right side of the river.
# The boat is on the right side of the river as a startstate

animals = ['chicken', 'fox']
objects = ['grain']

print ("Here is the state of the river-world:")
print ("[Chicken Fox Grain Man ---\ \_ _/ ___________/---]\n")
print ("You need to get the chicken, fox and grain across the river")
print ("But there are some rules: \nThe fox cannot be alone with the chicken. \nThe chicken cannot be alone with the grain. \n Only one of " + ', '.join(map(str, animals)) + " and " + ', '.join(map(str, objects)) + " can go in the boat with the man at the same time")

# Ask the user for a input, chicken, fox or grain.
putin = raw_input("\nSelect chicken/fox/grain by typing here: ")
# Convert the input to lowercase
putin = putin.lower();
# Check if the input is either chicken, fox or grain
while (putin != "chicken" and putin != "fox" and putin != "grain"):
    # If not correct input, print the input
    print(putin);
    # Print that the input is invalid, ask for a new input
    putin = input("Your choice is invalid. Please enter your choice (chicken/fox/grain): ");
    # Convert the new input to lowercase
    putin = player.lower();
    
# If the user's input is 'chicken', transport the chicken.
if putin == 'chicken':
    print ("\nYou have chosen to transport the " + putin + " across the river")
    print ("[Fox Grain ---\ \_ "+putin+" man _/ ___________/---]")
    print ("The " + putin + " is now on the right side of the river")
    
# If the user's input is 'fox', transport the fox
elif putin == 'fox':
    print ("You have chosen to transport the " + putin + " across the river")
    print ("[Chicken Grain ---\ \_ "+putin+" man _/ ___________/---]")
    print ("The " + putin + " is now on the right side of the river")
    
# If the user's input is 'grain', transport the grain
elif putin == 'grain':
    print ("You have chosen to transport the " + putin + " across the river")
    print ("[Chicken Fox ---\ \_ "+putin+" man _/ ___________/---]")
    print ("The " + putin + " is now on the right side of the river")

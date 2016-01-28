# Oppgavesoppgave #1, uke 3.
# Gruppenr.: 13
#Gruppemedlemmer: Morten Amundsen, Nora Krogh, Erlend Saetre, Marius Fosseli, Joakim Kilen, Tina Kvist
'''
Imports the random module to generate a random computer choice
'''
import random;

'''
User input, checks if input is valid
'''

player = input("Please enter your choice (rock/paper/scissors): ");
player = player.lower();
while (player != "rock" and player != "paper" and player != "scissors"):
    print(player);
    player = input("Your choice is invalid. Please enter your choice (rock/paper/scissors): ");
    player = player.lower();
    
'''
Computers (bot) choice. A random choice is taken by using the random module.
Generates a random number from 0-2, and converts the number into a rock, paper or scissors
'''
botInt = random.randint(0,2);
if (botInt == 0):
    bot = "rock";
    print "The bot chose rock."
elif (botInt == 1):
    bot = "paper";
    print "The bot chose paper."
elif (botInt == 2):
    bot = "scissors";
    print "The bot chose scissors."
else:
    bot = "Error occured. Please play again";
    
'''
Selects a winner.
Checks if the choices of player and bot are the same. If they are, prints "tie".
If not, runs through the list until a winner is decided.
'''
# checks if the players and the bots selection is the same. If true, prints tie
if (player == bot):
    print("You have tied!");
    
# if the player chose rock:
elif (player == "rock"):
    if (bot == "paper"):
        print("The bot won..");
    else:
        print("You beat the bot!");
        
# if the player chose paper:
elif (player == "paper"):
    if (computer == "rock"):
        print("You beat the bot!");
    else:
        print("The bot won..");

# if the player chose scissors:
elif (player == "scissors"):
    if (computer == rock):
        print("The bot won..");
    else:
        print("You beat the bot!");
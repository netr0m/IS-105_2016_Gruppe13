# Oppgavesoppgave #1, uke 3.
# Gruppenr.: 13
# Gruppemedlemmer: Morten Amundsen, Nora Krogh, Erlend Saetre, Marius Fosseli, Joakim Kilen, Tina Kvist

'''
Imports the random module to generate a random computer choice
'''

import random

player = input('Please enter your choice (rock/paper/scissors): ')
player = player.lower()
while player != 'rock' and player != 'paper' and player != 'scissors':
    print player
    player = \
        input('Your choice is invalid. Please enter your choice (rock/paper/scissors): '
              )
    player = player.lower()

botInt = random.randint(0, 2)
if botInt == 0:
    bot = 'rock'
elif botInt == 1:
    bot = 'paper'
elif botInt == 2:
    bot = 'scissors'
else:
    bot = 'Error occured. Please play again'

# checks if the players and the bots selection is the same. If true, prints tie

if player == bot:
    print 'You have tied!'
elif player == 'rock':

# if the player chose rock:

    if bot == 'paper':
        print 'The bot won..'
    else:
        print 'You beat the bot!'
elif player == 'paper':

# if the player chose paper:

    if computer == 'rock':
        print 'You beat the bot!'
    else:
        print 'The bot won..'
elif player == 'scissors':

# if the player chose scissors:

    if computer == rock:
        print 'The bot won..'
    else:
        print 'You beat the bot!'

print 'You chose ' + player + '\nThe computer chose ' + computer

			
# -*- coding: utf-8 -*-
# Gruppe 13: Morten Amundsen, Nora Krogh, Erlend Sætre, Joakim Kilen, Marius Fosseli

# The message to encode
message = raw_input("Write a message to encode here: ")
# message = "BCCACBCCCCCCCCCCCACCCA"

def code():
    '''
    Implements an initial table for LZW algorithm 
    '''
    tab = {}
    tab[1] = 'a'
    tab[2] = 'b'
    tab[3] = 'c'
    tab[4] = 'd'
    tab[5] = 'e'
    tab[6] = 'f'
    tab[7] = 'g'
    tab[8] = 'h'
    tab[6] = 'i'
    tab[9] = 'j'
    tab[10] = 'k'
    tab[11] = 'l'
    tab[12] = 'm'
    tab[13] = 'n'
    tab[14] = 'o'
    tab[15] = 'p'
    tab[16] = 'q'
    tab[17] = 'r'
    tab[18] = 's'
    tab[19] = 't'
    tab[20] = 'u'
    tab[21] = 'v'
    tab[22] = 'w'
    tab[23] = 'x'
    tab[24] = 'y'
    tab[25] = 'z'
    
    return tab

# Function to encode the message that the user typed
def encode(message):
    tab = code()
    string = ""
    code4string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in tab.values():
            string = string + symbol
        else:
            for key, value in tab.iteritems():
                if value == string:
                    code4string.append(key)
            tab[max(tab.keys())+1] = string + symbol
            string = symbol
    for key, value in tab.iteritems():
        if value == string:
            code4string.append(key)
    # Print the table
    print tab
    return code4string
# Print the encoded message   
print encode(message)
 

'''
def test():
    testMessage = "This is a test message. Hi."
    print encode(testMessage)
'''
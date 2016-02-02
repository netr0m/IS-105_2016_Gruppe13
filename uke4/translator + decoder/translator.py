# -*- coding: utf-8 -*-
'''
GRUPPENR: 13
STUDENTER: Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fossli, Joakim Kilen
'''

# This script translates from Binary to ASCII, and vice versa.
# Translator:

def translator ():
    b2a = {}
    
    for i in range(0, 128):
        b2a[format(i, '08b')] = chr(i)
        
    # Return the outcome
    return b2a


# Get the binary code from a String
def binaryToAscii(bin2asc, binCode):
    
    # The sentence generated in ASCII
    ascSentence = ""
    shortBin = ""
    
    # Run a loop through the binary code, number by number, and generate ASCII characters
    for c in binCode:
        
        if len(shortBin) == 8:
            ascSentence = ascSentence + bin2asc[shortBin]
            shortBin = "";
            
        else:
            shortBin = shortBin + c
            
    return ascSentence


def asciiToBinary(bin2asc, text):
    reversed = {}
    # Reversing the binary mapping
    for k, v in bin2asc.iteritems():
        reversed[v] = reversed.get(v, [])
        reversed[v].append(k)
        
    
    binSentence = ""
    # Create a sentence in binary
    for c in text:
        
        letter = str(reversed[c]).strip("['']")
        binSentence = binSentence + letter
        
    return binSentence

# The binary number you'd like to translate to String text
print binaryToAscii(translator(), '011101000011001010011100110011101000')
# The String text you'd like to translate to Binary number
print asciiToBinary(translator(), "Have a nice day")

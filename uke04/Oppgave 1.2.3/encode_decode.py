# -*- coding: utf-8 -*-
'''
GRUPPENR: 13
STUDENTER: Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fossli, Joakim Kilen
'''

def code():
    '''	
    Implements a code: ASCII mapping from binary string to ASCII string
    and the other way around. Load the tables in memory. 
    '''
    
    binary = {}
    ascii = {}
    
    # Generate ascii code
    for i in range(0,128) :
        ascii[format(i,'08b')] = chr(i)
    
    
    # Reverse the ascii code, this will be binary
    for k, v in ascii.iteritems():
        binary[v] = binary.get(v, [])
        binary[v].append(k)   
    
    return ascii

def encode(string):
    '''
    Encode some text using text from a source
    '''
    # Go through each character in a given string
    return "".join([format(ord(char),'#010b')[2:] for char in string])
            
def decode(sourcecode,n, ascii):
    '''
    Decode a sourcecode using chunks of size n
    '''
    
    sentence = ""    
    
    f = open(sourcecode, mode='rb') # Open a file with filename <sourcecode>
    while True:
        chunk = f.read(n)           # Read n characters at time from an open file
        if chunk == '':             # This is one way to check for the End Of File in Python 
            break
        if chunk != '\n':
            
            # Create a sentence
            sentence = sentence + ascii[chunk]
            
    return sentence

def test():
    '''
    A placeholder for some test cases.
    It is recommended that you use some existing framework, like unittest,
    but for a temporary testing in a development version can be done 
    directly in the module.
    '''
    
    print "Encoded from ASCII String to Binary:"
    # The ASCII String to convert to Binary
    print encode("Norway stun Poland 30:28 and spoil Bielecki's birthday party.")
    print
    print "Decoded from Binary to ASCII String:"
    # The txt-file to convert from Binary to ASCII
    print decode('sourcecode.txt', 8, code())

test()
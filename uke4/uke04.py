# -*- coding: utf-8 -*-
'''
Module med eksempler i uke 04 (informasjonsteori)
Løsninger for klasseoppgavene 25.01.2016 implementeres her
Løsningsforslag innleveres i gruppe-repositorien.
GRUPPENR: ...
STUDENTER: ...
'''

def code():
    '''
    Implements a code: ASCII mapping from binary string to ASCII string
    and the other way around. Load the tables in memory. 
    '''
    ascii = {'01000001':'A', ...}
    binary = {'A':'01000001', ...}
    return (ascii, binary) # A suggested way to load tables in memory

def encode():
    pass

def decode(sourcecode,n):
    '''
    Decode a sourcecode using chunks of size n
    '''
    # You will need a dictionary holding the mapping between binary string and ASCII chars
    
    f = open(sourcecode, mode='rb') # Open a file with filename <sourcecode>
    while True:
        chunk = f.read(n)           # Read n characters at time from an open file
        if chunk == '':             # This is one way to check for the End Of File in Python 
            break
        if chunk != '\n':
            # Your code goes here, process is a placeholder, process chunk
            # Return the decoded message
            pass

def test():
    '''
    A placeholder for some test cases.
    It is recommended that you use some existing framework, like unittest,
    but for a temporary testing in a development version can be done 
    directly in the module.
    '''
    pass
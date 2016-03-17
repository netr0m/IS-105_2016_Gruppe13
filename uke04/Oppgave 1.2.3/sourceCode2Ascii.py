## -*- coding: utf-8 -*-
'''
Module med eksempler i uke 04 (informasjonsteori)
Løsninger for klasseoppgavene 25.01.2016 implementeres her
Løsningsforslag innleveres i gruppe-repositorien.
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
    
    return ascii # A suggested way to load tables in memory

def encode():
    pass

def decode(sourcecode,n, ascii):
    '''
    Decode a sourcecode using chunks of size n
    '''
    # You will need a dictionary holding the mapping between binary string and ASCII chars
    
    sentence = ""    
    
    f = open(sourcecode, mode='rb') # Open a file with filename <sourcecode>
    while True:
        chunk = f.read(n)           # Read n characters at time from an open file
        if chunk == '':             # This is one way to check for the End Of File in Python 
            break
        if chunk != '\n':
            
            setence = ""            # The ascii sentence generated
            
            # create a s
            sentence = sentence + ascii[chunk]
            
    return sentence

def test():
    '''
    A placeholder for some test cases.
    It is recommended that you use some existing framework, like unittest,
    but for a temporary testing in a development version can be done 
    directly in the module.
    '''
    
    print decode('c:/users/morten/desktop/IS-105/is-105_2016_gruppe13/uke4/oppgave 1.2.3/sourcecode.txt', 8, code())

test()
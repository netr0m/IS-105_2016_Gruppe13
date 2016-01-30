# -*- coding: utf-8 -*-
'''
Module med eksempler i uke 04 (informasjonsteori)
Løsninger for klasseoppgavene 25.01.2016 implementeres her
Løsningsforslag innleveres i gruppe-repositorien.
GRUPPENR: 13
STUDENTER: Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fossli, Joakim Kilen, Tina Kvist
'''


def code_and_decode(bin):
    bin ='01001110011011110111001001110111011000010111100100100000011100110111010001110101011011100010000001010000011011110110110001100001011011100110010000100000001100110011000000111010001100100011100000100000011000010110111001100100001000000111001101110000011011110110100101101100001000000100001001101001011001010110110001100101011000110110101101101001001001110111001100100000011000100110100101110010011101000110100001100100011000010111100100100000011100000110000101110010011101000111100100101110'
    length = 8
    input_l = [bin[i:i+length] for i in range(0,len(bin),length)]
    
    input_c = [chr(int(c,base=2)) for c in input_l]
    print ''.join(input_c)

def test():
    '''
    A placeholder for some test cases.
    It is recommended that you use some existing framework, like unittest,
    but for a temporary testing in a development version can be done 
    directly in the module.
    '''
    pass

code_and_decode (bin)

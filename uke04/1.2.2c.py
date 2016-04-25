#!/usr/bin/python
# Decoding of the binary numbers
mapping = { '0': 'X', '10': 'Y', '11': 'Z' }

input_binary = "00101001100000"
output_string = ''

i = 0
while i < len(input_binary):
    if input_binary[i] == '0':
        output_string += mapping[input_binary[i]]
        i = i + 1
        continue

    output_string += (mapping[input_binary[i:(i + 2)]])
    i = i + 2
print output_string


# Encoding of the text
mapping = { 'X': '0', 'Y': '10', 'Z': '11' }

input_text = "XXYYXZXXXXX"
output_binary = ''

i = 0
while i < len(input_text):
    if input_text[i] == 'X':
        output_binary += mapping[input_text[i]]
        i = i + 1
        continue

    output_binary += (mapping[input_text[i:(i + 1)]])
    i = i + 1
print output_binary
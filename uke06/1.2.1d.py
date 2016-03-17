#!/usr/bin/python
mapping = { '0': 'C', '10': 'A', '11': 'B' }

input_binary = "110010011000000000001000010"
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
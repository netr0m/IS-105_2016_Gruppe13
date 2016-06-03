#!/usr/bin/python
# Keeps an overview of which number belonging to which letter.
mapping = { '0': 'X', '10': 'Y', '11': 'Z' }

# The binary to translate to ascii
input_binary = "00101001100000"
# The field where the ascii result is going to be stored later on
output_string = ''

i = 0
# While-loop, as long as "i" is less than the length of the string stored in "input_binary"
while i < len(input_binary):
    if input_binary[i] == '0':
        output_string += mapping[input_binary[i]]
        # Increase the value of "i" by 1
        i = i + 1
        continue

    output_string += (mapping[input_binary[i:(i + 2)]])
    # Increase the value of "i" by 2
    i = i + 2
# Print the result/the translated string
print output_string

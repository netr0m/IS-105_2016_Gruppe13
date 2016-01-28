# Oppgave 1.2.2c fra uke 4
# Gruppe 13
mapping = { '0': 'X', '10': 'Y', '11': 'Z' }

input_string = "00101001100000"
output_string = ''

i = 0
while i < len(input_string):
    if input_string[i] == '0':
        output_string += mapping[input_string[i]]
        i = i + 1
        continue

    output_string += (mapping[input_string[i:(i + 2)]])
    i = i + 2
print output_string
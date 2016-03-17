
i = format(56,'08b')
print (i)

binary2ascii = {}
for i in range(0, 128):
    binary2ascii[format(i, '08b')] = chr(i)

ascii2binary = {}
for i in range(0, 128):
    ascii2binary[chr(i)] = format(i, '08b')


print(binary2ascii)
print("\n")
print(ascii2binary)
print("\n")

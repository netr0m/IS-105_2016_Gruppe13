text = '010001011010100011110010000101110101010111010100111010101000101011111'
codes = {'0': 1, '10': 2, '110': 3, '1110': 4, '11110': 5, '11111': 6}

code = ''
for char in text:
    code += char
    if code in codes:
        print codes[code],
        code = ''
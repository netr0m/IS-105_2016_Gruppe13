code4string = []

def code():
    '''
    The initial table for the LZW algorithm
    '''
    
    tab1 = {}
    # Generate 128 text-elements
    for i in range(0, 128):
        tab1[1] = chr(i)
    return tab1

def encode(string, byte, tab):
    global code4string
    symbol = byte
    
    '''
    Check if string & symbol is already in the table (tab). If it is; string = string + symbol
    '''
    if (string + symbol) in tab.values():
        string = string + symbol
    else:
        for key,value in tab.iteritems():
            if value == string:
                code4string.append(key)
                
        # Sets a limit, defining where it should start over in the table
        if (len(tab) >= 4095):
            tab = code()
        
        # Add string + symbol to the table (tab)
        tab[max(tab.keys())+1] = string + symbol
        string = symbol
        
    return {'tab':tab, 'string':string}

# Open a file to compress
def run(inFile, outFile):
    # Open the inputfile
    f = open(inFile, 'r')
    # Open the outputfile, 'write'
    outFile = open(outFile, 'w')
    temporary = {}
    # Add text-elements to the table (tab)
    tab = code()
    # String to hold the current byte
    byte = ""
    # String to hold the last byte; so that it can be added to the table (tab) at a later time
    string = ""
    # Read the first byte
    byte = f.read(1)
    
    # Call for the global code4string
    global code4string
    
    # Run the byte we read earlier
    if (byte != ""):
        # Encoding the first byte
        temporary = encode(string, byte, tab)
        # Adds the returned values to the strings
        string = temporary['string']
        tab = temporary['tab']
        
    # Run; as long as there are bytes in the file
    while (byte != ""):
        # Get a byte
        byte = f.read(1)
        # Write to the file
        if (byte != ""):
            # Encode
            temporary = encode(string, byte, tab)
            # Adds the returned values to the variables
            string = temporary['string']
            tab = temporary['tab']
    
    for key, value in tab.iteritems():
        if value == string:
            # Append the key to output table (tab)
            code4string.append(key)
    
    outFile.write(''.join(map(str,code4string)))
    
    toString = ''.join(map(str,code4string))
    return toString

# run('inFile.txt', 'output.txt') What file you want to encode, and the name of the file to be created
# Change 'hamlet.txt' to 'shakespeare.txt' to encode complete_shakespeare.txt
if __name__ == '__main__':
    run('shakespeare.txt', 'output1.txt')
            
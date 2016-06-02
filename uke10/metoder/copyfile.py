import mmap
import shutil
import contextlib

# Copy file contents into a new file, named 'lorem_copy.txt'
shutil.copyfile('original.txt', 'original_copy.txt')

# The word to look for in the file
word = 'testing'
reversed = word[::-1]

# Open the new file
with open('original_copy.txt', 'r+') as f:
    # Since this is done using the access setting "ACCESS_WRITE",
    # changes will be saved to the disk.
    # If done using "ACCESS_COPY", changes will not be saved to disk
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)) as m:
        # Prints the original memory of the file
        print 'Memory Before:', m.readline().rstrip()
        # Prints the original content of the file
        print 'File Before  :', f.readline().rstrip()
        print
        # Finds the word stored in the variable "word".
        # Reverses the word
        m.seek(0) # rewind
        loc = m.find(word)
        m[loc:loc+len(word)] = reversed
        
        m.seek(0) # rewind
        # Prints the memory of the file after reversing the word
        print 'Memory After :', m.readline().rstrip()

        f.seek(0)
        # Prints the content of the file after reversing the word
        print 'File After   :', f.readline().rstrip()
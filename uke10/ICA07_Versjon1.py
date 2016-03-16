# -*- coding: utf-8 -*-
# ICA07 / Uke 10
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen
"""
Kilder:
http://www.tutorialspoint.com/python/os_remove.htm
https://pymotw.com/2/mmap/
https://docs.python.org/2/library/mmap.html
"""

# Filesystem
# Import the Memory-map module etc.
import mmap
import shutil
import contextlib
import os

userchoice = raw_input("""Select one of the options below:
1. Create file
2. Read file
3. Copy file
4.Search and replace in file
5. Rename a file
6. Delete a file\n
""")

if userchoice == "1":
    """
    First of all, we are going to create a file with some given content.
    Write an example file (creates newfile.txt)
    """
    with open("newfile.txt", "wb") as f:
        # Writes the sentence inside ("") to the specified file
        f.write("Karamellen min liker poteter, og du heter Ove Sundberg\n")
        
        # Opens the specified file
        with open("newfile.txt", "r+b") as f:
            # Memory-map the file, size 0 means the whole file
            mm = mmap.mmap(f.fileno(), 0)
            # Read the content via standard file methods
            print "The content of the file is:\n"
            print mm.readline()  # Prints the first line of text in the specified file
            # Close the map
            mm.close()
        
elif userchoice == "2":
    """
    Now we want to read the content of a file
    This can be done by using two different methods;
    The slice function, or the read function
    """
    # Opens 'lorem.txt', reads the file
    with open('lorem.txt', 'r') as f:
        # Gives access to read
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            # Prints the first 10 bytes in the file by using the read function
            print '\n1st   10 bytes via read:', m.read(10)
            # Prints the second set of 10 bytes (bytes from 11-20) in the file by using the read function
            print '2nd   10 bytes via read:', m.read(10)
            # Prints tue third set of 10 bytes (bytes from 21-30) in the file by using the read function
            print '3rd   20 bytes via read:', m.read(20)
            # Closes the mmap
            m.close()
            
            # Opens 'lorem.txt' again, reads the file
            with open('lorem.txt', 'r') as f:
                # Gives access to read
                with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
                    # Prints all of the content in the file
                    print '\nAll content in the file:\n', m.read(1000)
                    
                    # Prints the first 10 bytes in the file by using the slice function
                    print '\nFirst 10 bytes via slice:', m[:10]
                    # Prints the second set of 10 bytes in the file by using the slice function
                    print 'First 20 bytes via slice:', m[:20]
                    # Prints the second set of 10 bytes in the file by using the slice function
                    print 'First 30 bytes via slice:', m[:30]
                    print
                    
elif userchoice == "3":
    """
    Well, now that we have created a file and looked at the content of a file,
    we're going to make a copy of a file as a backup.
    """
    # Copy file contents into a new file, named 'lorem_copy.txt'
    shutil.copyfile('original.txt', 'original(1).txt')
    print "\nThe file has been copied successfully!"
    

elif userchoice == "4":    
    """
    Okay, so now we're going to look for a specific word inside of a specific file.
    In other words, searching. When this word is found, we are going to reverse the word
    (backwards), and replace the original word with the reversed one.
    """
    # The word we're looking for in the file
    word = 'testing'
    reversed = word[::-1]
    
    # Open the new copy of the file
    with open('original(1).txt', 'r+') as f:
        # Since this is done using the access setting "ACCESS_WRITE",
        # changes will be saved to the disk.
        # If done using "ACCESS_COPY", changes will not be saved to disk
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)) as m:
            # Prints the original memory of the file
            print '\nMemory Before:', m.readline().rstrip()
            # Prints the original content of the file on the disk
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
            # Prints the content of the file on the disk after reversing the word
            print 'File After   :', f.readline().rstrip()
            
elif userchoice == "5":
    # Define a file to rename
    aFile = raw_input("Select a file, e.g. 'test.txt': ")

    # Rename the specified file, "renamed.txt" is the new name
    os.rename(aFile, "renamed.txt")
    
else:
    # Use the OS module to delete a specific file
    # Deletes the file "deleteme.txt"
    os.remove("deleteme.txt")
# -*- coding: utf-8 -*-
# ICA07 / uke 10
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Import the Memory-map module
import mmap

# Create a new file, with content
# Write an example file (creates newfile.txt)
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
# -*- coding: utf-8 -*-
# ICA07 / uke 10
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Import the Memory-map module
import mmap


# Write an example file (creates test1.txt)
with open("test1.txt", "wb") as f:
    # Writes the sentence inside ("") to the specified file
    f.write("Karamellen min liker poteter, og du heter Ove Sundberg\n")

# Opens the specified file
with open("test1.txt", "r+b") as f:
    # Memory-map the file, size 0 means the whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read the content via standard file methods
    print mm.readline()  # Prints the first line of text in the specified file
    # Read content in the file via slice notation
    print mm[:10]  # Prints the first mm[:x] letters, here the first 10 characters (Karamellen)
    # Update the content in the file using slice notation;
    # Beware that the new content must have the same size as the content being replaced
    # mm[42:] means it replaces the content 42 characters from the beginning
    # (There are 42 characters from the first word "Karamellen min(...)" to the words "Ove Sundberg")
    mm[42:] = "Alf Hestesen\n"
    # Read the file again using standard file methods
    mm.seek(0)
    print mm.readline()  # Prints the first line again, but this time the edited/updated version
    # Close the map
    mm.close()
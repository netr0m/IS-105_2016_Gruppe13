import os

aFile = raw_input("Select a file, e.g. 'test.txt' ")

os.rename(aFile, "renamed.txt")
# -*- coding: utf-8 -*-
# ICA07 / Uke 10
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Joakim Kilen, Erlend Sætre
# Ikke-fungerende, bare test

# For filesystem
class filesystem():
    
    # Check if the node is a folder
    def is_dir(name):
        self.name = name
        if name == dir:
            print "The node is a folder"
        else:
            print "The node is not a folder"
        
    # Check if the node is a file
    def is_file(name):
        self.name = name
        if name == file:
            print "The node is a file"
        else:
            print "The node is not a file"
        
    # Search for a filename, and return if existing
    def get(filename):
        self.filename = filename
        if filename == filename:
            print filename
        
    # Add a file, and file content, to a list of files
    def add(file):
        self.file = file
        
    # Remove a file along with its contents from a list of files
    def remove(file):
        self.file = file
        self.list = list
        
    # Rename a file
    def rename(file, name):
        self.file = file
        self.name = name
        
    # Copy a file
    def copy(file, location):
        self.file = file
        self.location = location
        
    # Print statistics, overview
    def stat(files):
        self.files = files
        
    # Read contents of a file
    def read(file):
        self.file = file
    
    # Create a folder
    def mkdir(dir):
        self.dir = dir
        
    # Change to a specific folder
    def chdir(dir):
        self.dir = dir
        
    # Delete a specific folder
    def rmdir(dir):
        self.dir = dir
        
    # Delete a specific file
    def rm(file):
        self.file = file
        
    # List contents of the selected folder
    def ls(dir):
        self.dir = dir
        
    # Create a new file, possibly with content
    def create(file):
        self.file = file
        
    # Read and print the contents of a file
    def read(file):
        self.file = file
        print file
        
    # Move a file, basically the same as renaming it
    def mv(file, location):
        self.file = file
        self.location = location
    
    # Create a copy of the file
    def cp(file):
        self.file = file
        filename += "(2)"
        
    # Help
    def help():
        print filesystem
        
    def exit():
        engine.runAndWait()
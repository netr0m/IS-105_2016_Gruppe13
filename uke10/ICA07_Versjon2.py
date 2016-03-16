# -*- coding: utf-8 -*-
# FILSYSTEM
# Denne versjonen er basert på kode fra http://technoslab.blogspot.no/2014/08/write-python-program-for-creating.html
# Gruppe 13: Morten Amundsen, Nora Krogh, Marius Fosseli, Erlend Sætre, Joakim Kilen

# Import setninger
import shelve, time, sys


print "Type a commando to begin. For help, type 'help'"

# Class for File
class File(object):
    
    # Initialize the class File, with parameters name, type(file or dir), text
    def __init__(self, name, type, parent=None, text=''):
        self.list = []
        self.name = name
        self.type = type
        self.time = int(time.time())
        self.parent = parent
        self.text = text
    
    # Check if the node is a file    
    def is_file(self, name):
        for node in self.list:
            if node.name == name:
                return True
            return False
    
    # Check if the node is a directory    
    def is_dir(self, name):
        if(self.is_file(name)) and self.get(name).type == 'dir':
            return True
        return False

    def get(self, name):
        for node in self.list:
            if node.name == name:
                return node
    
    # Add the node to a list        
    def add(self, name, type, text=''):
        self.list.append(File(name, type, self, text))
    
    # Remove the file from a list    
    def remove(self, name):
        self.list.remove(self.get(name))
    
    # Rename the file    
    def rename(self, name):
        self.name = name
    
    # Copy the file    
    def copy(self, src, dest):
        src = self.get(src)
        self.add(dest, src.type, src.text)
    
    # Print stats for a list   
    def stat(self):
        print 'Listing', self.name
        for node in self.list:
            print 'Name:', node.name, '; Created:', node.time, '; Type:', node.type
    
    # Read the file name and content, print it        
    def read(self):
        print 'Reading file:', self.name
        print self.text

# Class for the filesystem        
class FileSystem(object):
    # Available commands
    COMMANDS = ['ls', 'mkdir', 'chdir', 'cd', 'rmdir', 'create', 'read', 'rm', 'mv', 'cp', 'help', 'exit']
    
    # Initialize the class
    def __init__(self):
        self.io = shelve.open('file.sys', writeback=True)
        if self.io.has_key('fs'):
            self.root = self.io['fs']
        else:
            self.root = File('/', 'dir')
        self.curr = self.root
    # Make a directory    
    def mkdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'mkdir - Make a new directory'
            # How to use it
            print 'How to use: mkdir <dir_name>'
        else:
            name = cmd[1]
            # If the node is a file, set False
            if self.curr.is_file(name) == False:
                # Create the directory, type 'dir'
                self.curr.add(name, 'dir')
            else:
                # If there already exists a directory with the given name,
                # print " name + already exists"
                print name, ' - already exists.';
    
    # Change directory            
    def chdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'chdir - Change to a different directory.'
            # How to use it
            print 'How to use: chdir <dir_name>'
        else:
            name = cmd[1]
            if name == '..':
                if self.curr.parent is not None:
                    self.curr = self.curr.parent
            # If the node is a directory
            elif self.curr.is_dir(name):
                # Get directory name
                self.curr = self.curr.get(name)
            else:
                # Otherwise, if the given name is invalid,
                # print "name + invalid directory"
                print name, ' - invalid directory.'
    
    # Delete a directory            
    def rmdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'rmdir - Remove a directory'
            # How to use it
            print 'How to use: rmdir <dir_name>'
        else:
            name = cmd[1]
            # If the node is a directory;
            if self.curr.is_dir(name):
                # Remove it
                self.curr.remove(name)
                # Print confirmation of deletion
                print 'Directory deleted.'
            else:
                # Otherwise, if the given name is invalid;
                # Print "name + invalid directory"
                print name, ' - invalid directory.'
    
    # Delete a file            
    def rm(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'rm - Remove a file'
            # How to use it
            print 'How to use: rm <file_name>'
        else:
            name = cmd[1]
            # Check if the node is a file, and not a directory;
            if self.curr.is_file(name) and not self.curr.is_dir(name):
                # Remove the file
                self.curr.remove(name)
                # Print confirmation of deletion
                print 'File deleted.'
            else:
                # Otherwise, if the given name is invalid;
                # Print "name + invalid file"
                print name, ' - invalid file.'
    
    # List all content            
    def ls(self, cmd):
        if(len(cmd) > 1):
            # Description of the command
            print 'ls - List files in the directory'
            # How to use it
            print 'How to use: ls'
        self.curr.stat()
    
    # Create a new file    
    def create(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'create - Create a new file'
            # How to use it
            print 'How to use: create <file_name>'
        else:
            name = cmd[1]
            # Add the file with a given name, type 'file', and given content
            self.curr.add(name, 'file', raw_input('Enter file content: '))
    
    # Read the name and content of a file        
    def read(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            # Description of the command
            print 'read - Read the contents of a file'
            # How to use it
            print 'How to use: read <file_name>'
        else:
            name = cmd[1]
            # Check if the node is a file
            if self.curr.is_file(name):
                # Get name and read it
                self.curr.get(name).read()
            else:
                # Otherwise, if the given name is invalid;
                # Print "name + invalid file"
                print name, 'invalid file'
    
    # Rename a file            
    def mv(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            # Description of the command
            print 'mv - Rename a file'
            # How to use it
            print 'How to use: mv <old_name> <new_name>'
        else:
            old_name = cmd[1]
            new_name = cmd[2]
            # Check if the node is a file
            if self.curr.is_file(old_name):
                # Rename the given file
                self.curr.get(old_name).rename(new_name)
            else:
                # Otherwise, if the given name is invalid;
                # Print "old_name + invalid file"
                print old_name, 'invalid file'
    
    # Make a copy of a file            
    def cp(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            # Description of the command
            print 'cp - Make a copy of a file'
            # How to use it
            print 'How to use: cp <src> <dest>'
        else:
            src = cmd[1]
            dest = cmd[2]
            # Check if the node is a file
            if self.curr.is_file(src):
                # Copy the file
                # Original filename and name of the copy
                self.curr.copy(src, dest)
            else:
                # Otherwise, if the given name of the original file is invalid;
                # Print "src + invalid file"
                print 'The file "' + src + '" does not exist'
    
    # Save the changes            
    def save(self):
        self.io['fs'] = self.root
        self.io.sync()
    
    # Print help
    # Prints a list of available commands
    def help(self, cmd):
        print """
        mkdir - Make a new directory
        ls - List files in the directory
        chdir - Change to a different directory
        rmdir - Remove a directory
        create - Create a new file
        read - Read the contents of a file
        mv - Rename a file
        cp - Make a copy of a file
        rm - Remove a file
        exit - Exit the program
        """
    # Exit the program
    def exit(self, cmd):
        sys.exit(0)
# Main        
def main():
    fs = FileSystem()
    while True:
        # Sets cmd as a raw_input for the user to enter
        cmd = raw_input('> ').split(' ');
        method = None
        try:
            method = getattr(fs, cmd[0])
        except AttributeError:
            # If the user enters something that is not in the list of commands
            print 'Invalid command. Please type "Help"'
        if method is not None and cmd[0] in FileSystem.COMMANDS and callable(method):
            method(cmd)
            fs.save()
        else:
            print 'Invalid command. Please type "Help"'
main()
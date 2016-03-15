import mmap
import shutil
import contextlib

# Read content of the file
# Opens 'lorem.txt', reads the file
with open('lorem.txt', 'r') as f:
    # Gives access to read
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        # Prints the first 10 bytes in the file by using the read function
        print '1st   10 bytes via read:', m.read(10)
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
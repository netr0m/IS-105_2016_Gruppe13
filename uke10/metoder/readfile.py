import mmap
import shutil
import contextlib


# Read file
# Opens 'lorem.txt', reads the file
with open('lorem.txt', 'r') as f:
    # Gives access to read
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        # Prints the first 10 bytes in the file by using the read function
        print 'First 10 bytes via read:', m.read(10)
        # Prints the first 10 bytes in the file by using the slice function
        print 'First 10 bytes via slice:', m[:10]
        # Prints the second set of 10 bytes (bytes from 11-20) in the file by using the read function
        print '2nd   10 bytes via read :', m.read(10)
        # Prints tue third set of 10 bytes (bytes from 21-30) in the file by using the read function
        print '3rd   20 bytes via read:', m.read(20)
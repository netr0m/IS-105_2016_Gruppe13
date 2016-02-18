import lzw

infile = lzw.readbytes("hamlet.txt")
compressed = lzw.compress(infile)
lzw.writebytes("output.lzw", compressed)

# Ten later
infile = lzw.readbytes("output.lzw", compressed)
uncompressed = lzw.decompress(infile)
for bt in uncompressed:
    do_something_awesome_with_this_byte(bt)
    
#Skrevet av Joakim Kilen

print ("This is a test to see if the number x is less than the number y."  )
x = raw_input("Please pick your first number, x: ")
y = raw_input("Now, please pick your second number, y: ")

if (x < y):
    print "x is not less than y, since %r is not less than %r." % (x, y)

else:
    print "x is less than, or equal to y, since %r is less than, or equal to %r" % (x, y)
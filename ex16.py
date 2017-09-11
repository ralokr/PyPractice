from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

#I have found that CTRL-C does not work with PyCharm.
raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
'''
While truncate() will truncate the file to the initial position 
in this case (as we haven't passed any size argument to the method),
keep in mind that opening a file in write mode will do the same.
This is why I have commented the call to truncate().
'''
#target.truncate()

target = open(filename,'w')
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")


print "I'm going to write these to the file."

target.write (line1 + "\n" + line2 + "\n" + line3 + "\n")

print ("And finally, we close it.")
target.close()

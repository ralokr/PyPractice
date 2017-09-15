from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #Seeks position 2 from the default (zero) position
    #f.seek(-10, 2) #the second parameter indicates that the interpreter will seek from the end. Look up 'whence'.

def print_a_line(line_count, f):
    print line_count , f.readline()
    #print line_count , f.readline(), # The comma at end prevents print statement from adding an implicit \n to the output.

current_file = open(input_file)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#in_file = open (from_file)
#indata = in_file.read()
indata = open(from_file).read()

'''
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
'''
#out_file = open (to_file,'w')
out_file = open (to_file,'w').write(indata)
#out_file.write(indata)

#print "Alright, all done."

'''
When I open the file and read/write on the same statement,
I need not call close() explicitly. Python does that automatically
once it has executed the read/write statement.
'''
#out_file.close()
#in_file.close()
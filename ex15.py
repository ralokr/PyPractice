#This imports the argv list. This list contains the command-line
#arguments passed to the script.
from sys import argv

#Here, we pass the name of the script and the file name
script, filename = argv

#Open the file without any arguments
txt = open(filename)

#Print out the file name in raw format.
print "Here's your file %r:" %filename
#Read the contents of the file and print them.
print txt.read()

print "Type the file name again:"
#Prompts the user to enter the same file name again.
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()

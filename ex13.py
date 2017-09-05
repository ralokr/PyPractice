from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

print "Is it raining? ",
answer = raw_input()

if answer == "Yes":
    print "Oh yes, it is!"

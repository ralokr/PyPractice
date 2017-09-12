#This is similar to the scripts that import argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#Or, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This takes just one argument
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two("Alok", "Rout")
print_two_again("Alok","Rout")
print_one("Alok Rout")
print_none()

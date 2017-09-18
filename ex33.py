def list_append(limit, jump):

	i = 0

	while i < limit:
		print "At the top, i is %d" % i
		numbers.append(i)

		i += jump
		print "Numbers now: ", numbers

		print "At the bottom, i is %d" % i

		if i >= limit:
			print "Reached the end of loop. Terminating now."


numbers = []
list_append(8,2)

print "The numbers: "

for num in numbers:
    print num

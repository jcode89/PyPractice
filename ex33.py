import operator
numbers= []
numbers1 = []
def loop(n, oper, m):
	i = 0
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
		i = oper(i, m)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		def loop1():
			# with range() you don't need the increment that you use in the while-loop above.
			# if you did use the increment it would take each number in the list range creates and add to it.
			for h in range(0, n, m):
				print "At the top h is %d" % h
				numbers1.append(h)
				print "Numbers now: ", numbers1
				print "At the bottom h is %d" % h
			return numbers1
	return loop1
	
sloop = loop(29, operator.add, 2)	
print "The numbers: "

for num in numbers:
	print num
	
	


sloop()
#loop1(29)
print "The new numbers: "

for num in numbers1:
	print num
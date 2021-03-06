import unittest
import hashmap


# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')
hashmap.set(states, 'Oregon', 'US')
hashmap.set(states, 'Florida', 'US')
hashmap.set(states, 'California', 'US')
hashmap.set(states, 'New York', 'US')
hashmap.set(states, 'Michigan', 'US')
# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'CA', 'San Diego')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'MI', 'Freezing')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'FL', 'Tampa Bay')
hashmap.set(cities, 'FL', 'Miami')
# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')
hashmap.set(cities, 'OR', 'Helena')
hashmap.set(cities, 'NY', 'Brooklyn')
#hashmap.delete(cities, 'NY')
# print out some cities
print '-' * 10
print "NY State has: %s " % hashmap.get(cities, 'NY')
print "FL State has: %s " % hashmap.get(cities, 'FL')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')

print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
#print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))

#print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
#hashmap.delete(cities, 'OR')
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."
	
# default values using //= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

#hashmap.dump(cities)
print '-' * 10
#hashmap.dump(states)
# The following assertions test if there is more than one value.
assert(hashmap.get(cities, 'NY') != 'New York')
assert(hashmap.get(cities, 'OR') != 'Portland')
assert(hashmap.get(states, 'Michigan') != 'MI')
assert(hashmap.get(states, 'Florida') != 'FL')
#assert(hashmap.get(cities, hashmap.get(states, 'Michigan'))in 'Detroit')
#assert(hashmap.get(cities, hashmap.get(states, 'Florida')) in 'Jacksonville')
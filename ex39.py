# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print"OR State has: ", cities["OR"]

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
		
print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print 'Sorry, no Texas.'
	
# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print "The city for the state of 'TX' is: %s" % city
print "But we will add it!"
print "And we are going to add a surprise!"
states.update({'Texas':'TX'})
cities.update({'TX':'San Antonio'})
states.setdefault('Louisiana','LA')
cities.setdefault('LA',[])
cities['LA'].append('New Orleans')
cities['LA'].append('Shreveport')
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
print '-' * 10
print "Maybe multiple values? How about a list of values?"
cities['TX'] = ['San Antonio', 'Houston', 'Dallas']
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
		
print '-' * 10
cars = {
    'Chevy': 'Malibu',
	'Ford': 'F150',
	'Honda': 'Civic',
	'Nissan': 'Sentra',
	'Toyota': 'Camry'
}

more_cars = {
    'Chevy': 'Camaro',
	'Chevy': 'Corvette',
	'Mazda': 'Spyder',
	'Rolls Royce': 'Grand'
	
}

cars.update(more_cars)

for key, value in cars.items():
    print "%s has value %s" % (key, value)
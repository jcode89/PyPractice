#Sets the variable cars equal to 100
cars = 100
#Sets the variable space_in_a_car equal to 4.0, which is a floating point and is necessary to ensure accuracy.
space_in_a_car = 4.0
#Sets the drivers variable equal to 30
drivers = 30
#Sets the variable passengers equal to 90
passengers = 90
#Sets the variable cars_not_driven equal to the difference of the variables cars and drivers.
cars_not_driven = cars - drivers
#Sets the variable cars_driven equal to whatever the variable drivers is set to.
cars_driven = drivers
#Sets the variable carpool_capacity equal to the product of cars_driven and space_in_a_car.
carpool_capacity = cars_driven * space_in_a_car
#Sets the variable average_passengers_per_car equal to the quotient of passengers and cars_driven.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#The above error appeared because the underscore in between car and pool is not supposed to be there.
#carpool is one word. It should read, average_passengers_per_car = carpool_capacity / passenger.
#Also, if you look at line 7 above you will see that carpool_capacity and car_pool_capacity are not the same.
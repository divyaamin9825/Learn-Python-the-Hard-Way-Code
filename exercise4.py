#Number of cars available
cars = 100
#number of passenger seats in a car
space_in_a_car = 4
#number of drivers available
drivers = 30
#Number of passengers to carpool
passengers = 90
#Number of cars that are empty/not driven by anyone
cars_not_driven = cars - drivers
#number of cars driven
cars_driven = drivers
#Number of people that can be carpooled
carpool_capacity = cars_driven*space_in_a_car
#Average number of passengers in each car
average_passenger_per_car = passengers/cars_driven
print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We have",passengers,"to carpool today")
print("We can transport",carpool_capacity,"passengers today")
print("We need to put about",average_passenger_per_car,"in each car") 
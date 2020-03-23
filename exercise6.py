# Variable defining the number of types of people
types_of_people = 10
# A variable that has a format string assigned to it, 
# which will put variable types_of_people when it is used in print() 
# or put in another string
x = f"There are {types_of_people} types of people."

# This is a variable that has a string "binary" assigned to it
binary = "binary"
# This is a variable that has a string "don't" assigned to it
do_not = "don't"
# This is a variable that has an format string assigned to it,
# which will put variables binary and do_not when used in print 
# or put in another string
y = f"Those who know {binary} and those who {do_not}."
# printing the strings x and y
print(x)
print(y)
# printing 2 f-strings that make use of x and y
print(f"I said {x}.")
print(f"But I also said '{y}'")

# Boolean variable named hilarious
hilarious = False
# This is a variable that has a string assigned to it
# This string looks normal but the {} will have the variable hilarious inserted into it
joke_evaluation = "Isn't that joke so funny?! {}"
# Inserts hilarious into joke_evaluation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#concatenation of e to w
print(w + e)
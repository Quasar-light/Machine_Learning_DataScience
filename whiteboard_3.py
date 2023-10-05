# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone 
#number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

#create a function that take the input of an array of numbers. Index into the array to from a phone number. Array will always 10 integers
#numbers input when called. Input must be what is expected in the problem
#plan 
#step1: create def caller(a):
#step2: f'({a[0:2]}) {a[3:5]}-{a[6:]}'                        calling to the value of the numbers, 
#can do simply a colon to indicate all values to the end from this number
#step3 call function caller()

def caller(a):

    return f'({a[0:2]}) {a[3:5]}-{a[6:]}'

print(caller([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    



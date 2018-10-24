# Lambda Functions

# Lambdas are unnamed, in-place functions

# You could write a regular function to multiply a number:
def mul(n):
    return n*n

print(mul(8))

# Or you can write a lambda statement:
mul = lambda n: n * n
print(mul(8))

# Loop over a list of items concisely with map(). Map accepts 2 arguments: a function and an iterable.
# An anonymous lambda function will be called on each item in the iterable.
my_list = [1,2,3,4,5,6,7,8,9]

multi = map(lambda n: n * n, my_list)
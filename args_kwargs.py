# Argument Unpacking: *args and **kwargs

# You can unpack Tuples and Lists into a set of individual components using the * operator
my_list = [1, 2, 3, 4, 5, 6]

def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
    return total


# A List or Tuple is classed as a single item when passed into a function. The * operator will unpack the argument into individual components
add(my_list)  # This will not work >>> ((1, 2, 3, 4, 5, 6), )
add(*my_list) # This will work >>> (1, 2, 3, 4, 5, 6)

# Use ** kwargs to unpack dictionaries
names = dict(first_name='Saur', last_name='Dash')

def print_name(first_name, last_name):
    msg = f'Hello {first_name} {last_name}'
    print(msg)
    return msg


print_name(names)   # Will not work
print_name(**names) # Will work
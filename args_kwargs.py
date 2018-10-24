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

# Dictionary unpacking becomes very useful when writing control flow

def calculate(**kwargs):
    # Lookup table of operations
    operations = {
        'add':      kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
        'divide':   kwargs.get('first', 0) / kwargs.get('second', 1)
    }
    
    # Perform calculation based on lookup table results
    calculation = operations[kwargs.get('operation', '')]
        
    # Output control flow
    if kwargs.get('make_float'):
        return '{} {}'.format(kwargs.get('message', 'The result is'), float(calculation))
    else:
        return '{} {}'.format(kwargs.get('message', 'The result is'), int(calculation))


# Parameters must be passed in this order:
# 1. Parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs

calculate(make_float=False, 
        operation='add',
        message='You just added',
        first=2,
        second=4)   # "You just added 6"

calculate(make_float=True, 
        operation='divide', 
        first=3.5, 
        second=5)   # "The result is 0.7"
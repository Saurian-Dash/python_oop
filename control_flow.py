# Concise if statements
# You can reduce the footprint of if statements using the following syntax:

# Long:
def long_age_check(age):

    if age < 18:
        message = 'Not eligible'
    else:
        message = 'Eligible'

    return age, message


# Short
def short_age_check(age):

    message = 'Not eligible' if age < 18 else 'Eligible'

    return (age, message)

print(short_age_check(32))


# Function Annotation
# You can expressely declare the data types a function will read and write:

def add_to_number(num: int, by: int = 1) -> tuple:

    return (num, num + by)


print(add_to_number(1, 2))
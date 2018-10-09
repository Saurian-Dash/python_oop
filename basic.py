# OOP Basics
import datetime as dt


class User:
  
  def __init__(self):
    
    self.user_id = int(dt.datetime.timestamp(dt.datetime.now()))
    print(f'New user [id: {self.user_id}] created at: {dt.datetime.now()}')

  @staticmethod
  # Staticmethod: if you do not access the instance or class
  def is_workday(day):
    
    return not (day.weekday() == 5 or day.weekday() == 6)


class Person(User):

  def __init__(self, 
               first_name, 
               last_name, 
               age, 
               gender, 
               nationality, 
               email):
    self.first_name  = first_name
    self.last_name   = last_name
    self.user_name   = f'{self.first_name} {self.last_name}'
    self.age         = int(age)
    self.gender      = gender
    self.nationality = nationality
    self.email       = email

  def __repr__(self):
    
    # You can generate a dictionary of the class directly with:
    return str(self.__dict__)

  @classmethod
  def from_string(cls, usr_str):

    first_name,  \
    last_name,   \
    age,         \
    gender,      \
    nationality, \
    email        \
    = usr_str.split(',')

    return cls(first_name,  \
               last_name,   \
               age,         \
               gender,      \
               nationality, \
               email)


person_01 = Person.from_string('Joe,Bloggs,47,M,British,joebloggs@yahoo.com')

print(User.is_workday(dt.date(2017,1,1)))


class Employee:

    company = 'omni_consumer_products'
    no_of_employees = 0
    raise_amount    = 1.04

    def __init__(self, 
                 first_name, 
                 last_name, 
                 salary):

        self.user_id    = int(dt.datetime.timestamp(dt.datetime.now()))
        self.first_name = first_name
        self.last_name  = last_name
        self.salary     = int(salary)

        Employee.no_of_employees += 1

        print(f'New user: [{self.first_name} {self.last_name}] created at: {dt.datetime.now()}')

    @property
    def full_name(self):

        return f'{self.first_name} {self.last_name}'
    
    @property
    def email(self):

        return f'{self.first_name}.{self.last_name}@{self.company}.com'.lower()
    
    @classmethod
    def from_string(cls, 
                    emp_str,
                    delimiter):

        first_name, last_name, salary = emp_str.split(delimiter)

        return cls(first_name, last_name, salary)

    
    @classmethod
    def set_raise_amount(cls, new_raise_amount):

        cls.raise_amount = new_raise_amount

        return cls.raise_amount

  # @classmethod
  # def fromtimestamp(cls, t):
    
  #   # Construct a date from POSIX timestamp
  #   y, m, d, hh, mm, ss, weekday, jday, dst = dt.datetime.localtime(t)

  #   return cls(y, m, d)

    @staticmethod
    # Staticmethod: if you do not access the instance or class
    def is_workday(day):
        
        return not (day.weekday() == 5 or day.weekday() == 6)


    def apply_raise(self):

        self.salary = int(self.salary * self.raise_amount)
        print(self.salary)

        return self.salary


    def jill_sandwich(self):

        print('OMG, does Barry tell everyone that story?')
  

    def __repr__(self):

        # __repr__ method must return a string, so cast dict to str:
        return str(self.__dict__)


saur = Employee('Saur', 'Dash', 40000)
barry = Employee('Barry', 'Burton', 50000)
jill = Employee('Jill', 'Valentine', 60000)

print(saur)
print(saur.full_name)
print(Employee.apply_raise(saur))

Employee.apply_raise(jill)
Employee.jill_sandwich(jill)
Employee.set_raise_amount(1.06)

print(Employee.raise_amount)

Employee.from_string('Jolyne,Kujo,70000', ',')
Employee.from_string('Hermes,Costello,40000', ',')


class Developer(Employee):

    def __init__(self, 
                first_name, 
                last_name, 
                salary,
                prog_lang): 
        
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, 
                first_name, 
                last_name, 
                salary,
                employees=None): 

        super().__init__(first_name,
                        last_name, 
                        salary)

        if employees == None:
            self.employees = []
        else:
            self.employees = employees


    def add_employee(self, emp):

        if emp not in self.employees:
            self.employees.append(emp)


    def remove_employee(self, emp):

        if emp in self.employees:
            self.employees.remove(emp)


    def print_employees(self):

        for e in self.employees:
            print('-->', e)


dev_01 = Developer('Jotaro','Kujo',56000,'Python')
emp_01 = Employee('Enrico', 'Pucci', 64000)
emp_02 = Employee('Weather', 'Report', 42000)
mng_01 = Manager('DIO', 'Brando', 999999999, [dev_01])

print(dev_01)
print(mng_01)

mng_01.add_employee(emp_01)
mng_01.add_employee(emp_02)
mng_01.print_employees()


# Class Testing

# isinstance(Obj, Class) - Boolean check if an object is an instance of a Class
# issubclass(sub-Class, Class) - Boolean check if a Class is a sub-Class of another


class Member:

    def __init__(self, 
                f_name, 
                l_name, 
                age):

        self.f_name = f_name
        self.l_name = l_name
        self._age   = max(int(age), 0)

    
    @property
    def full_name(self):

        return f'{self.f_name} {self.l_name}'


    @property
    def age(self):

        return self._age

    # Note: Getters and Setters relate to @Properties with same name (def <name>():)
    @age.setter
    def set_age(self, new_age):

        self._age = max(new_age, 0)

    @age.getter
    def get_age(self):

        return self._age
    


    @classmethod
    def from_string(cls, new_str, delimiter):

        f_name, \
        l_name, \
        age     \
        = new_str.split(delimiter)

        return cls(f_name, \
                   l_name, \
                   age)


    def __repr__(self):

        return f'Member({self.f_name}, {self.l_name}, {self.age})'


    def __str__(self):

        return f'User: {self.full_name} ({self.age} years old)'


mem_01 = Member.from_string('Foo,Fighters,40', ',')

print(mem_01)

# Method Resolution Order (MRO)

# Call the __mro__ attribute on a Class to display the resolution order of related Classes
# help(cls) also can be used to display MRO


#      (A)
#    /     \
#  (B)     (C)
#    \     /
#      (D)

class A:
    def do_something(self):
        print('Method defined in A')

class B(A):
    def do_something(self):
        print('Method defined in B')

class C(A):
    def do_something(self):
        print('Method defined in C')

class D(B, C):
    def do_something(self):
        print('Method defined in D')


thing = D()
thing.do_something()

# MRO stack returns the first occurrance of do_something()

print(D.__mro__)
print(D.mro())
help(D)

class GrumpyDict(dict):

    def __repr__(self):

        print('NONE OF YOUR BUSINESS!')
        return super().__repr__()

    def __missing__(self, key):

        print(f'WHATEVER {key} IS, IT\'S NOT HERE')

    def __setitem__(self, key, value):

        print('OMG WHY ARE YOU BOTHERING ME!?')
        super().__setitem__(key, value)
    
    

test_data = GrumpyDict({'name': 'Aeon', 'age': 37})

print(test_data)
print(test_data['location'])
test_data['city'] = 'Tokyo'
print(test_data)
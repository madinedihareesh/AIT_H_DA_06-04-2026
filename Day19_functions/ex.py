'''
functions:
Builtin functions
user defined functions

def name_function():
    block of code
'''

# simple fucntion: function without parameters/arrguments

def greeting():
    print('Hello world!')

greeting()

# functions with parameters/arguments:
def add(a,b): ##formal argguments
    print(a+b)

add(20,10) ##Actual arrguments (positional arrguments)
add(b=10,a=20) ##keyword arguments.

# fucntion with default arrguments
def sub(a,b,c=1): ##default arrguments
    print(a-b-c)

sub(10,5)    


sub(20,b=8,c=5)

# fucntions with postional only arrguments
def person(name,/,age,occ):
    print(f'my name is {name},my age is {age} and my occ is {occ}')

person('hareesh',age=50,occ='job')

# function with keyword only arrguments:
def sample(a,b,*,c):
    print(a,b,c)

sample(10,20,c=30)

# function with mixed keyword and positional arrguments:
def hello(a,b,/,*,c,d):
    print(a,b,c,d)

hello(10,20,c=30,d=40)    



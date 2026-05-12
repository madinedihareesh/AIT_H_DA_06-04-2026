def var_pfunction(*args):
    sum=0
    for i in args:
        if i%2==0:
            sum+=i
    print(sum)        

var_pfunction(1,2,3,4,5,6,7,8,9,10)     

def var_kfunction(**kwargs):
    for i in kwargs:
        print(kwargs[i])


var_kfunction(name='John',age=20,city='karala')


# functions with return statements
def Sample(a,b,c):
    d=a+b+c
    return d

print(Sample(10,20,30))

# function with multiple return statements
def Maths(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a//b
    return c,d,e,f

print(type(Maths(10,2)))

# Recursive function:
def fun(n):
    if n<=0:
        return 1
    else:
        return n*fun(n-1)
    
print(fun(5) )   


# nested functions:
def outter():
    def inner():
        print('Hello world')
    inner()

outter() 

def outter():
    def inner():
        print('Hello world')
    return inner

f=outter()
f()

# clouser
def outter(name,age):
    
    def inner():
        print(name,age)
    inner()

outter('Something',10)


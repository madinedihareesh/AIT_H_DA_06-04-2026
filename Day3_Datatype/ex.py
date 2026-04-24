'''
Primitive Datatypes: ## it can store single value
int (immutable)
float
complex
string
bool
Non primitive data types: ## it can store n no of elements
list
tuple
array
byte array ## sequentical data
set  ## non-seq data
dict
 '''
# a=10
# print(id(a))
# a=100
# print(id(a))

# l=[1,2,3,4]
# print(id(l))
# l.extend([5,6,7])
# print(l)
# print(id(l))

'''
0-0000
0000
   1

1-0001
0001
   1 10

2-0010

(0-9) decimal numbers
(0-7) 0,1,2,3,4,5,6,7
(0-15) A,B,C,D,E,F
'''
# a=10 ## everything in python is an object
# print(type(a))
# print(dir(a))

# # print(10+'10') ##1010. '10'-5 5
# print(bin(a))
# print(oct(a))
# print(hex(a))
# print(0b1010)
# print(0o12)
# print(0xa)

# f=12.59
# print(type(f))
# print(f.__sizeof__())
# f1=1259e-2 ## e=10 -2 -100*1259
# print(f1)
# f1=1259e2 ## 100*1259= 125900.00
# print(f1)

# b=True ##1
# print(b)
# b1=False ##0
# print(b1)

s='AchieversIT'
s1="Hello World"
s2="""Hi there, How are you!
i am doing grate
"""
s3='''Hi there! Hello world
this is my first multiline string
'''
print(s1)
print(s)
print(s2)
print(s3)

c=10+9j ##real number+imaginary number(i(sqrt(-1)))

# int (string,bool,complex,float)
# str (int,bool,complex,float)
# bool (int,str,complex,float)
#float(int,str,comple,float)
#complex(int,str,bool,float)
'''
int() ##predeifined / bulit-in
str()
float()
bool()
complex
'''
# int to other data types
# a=10
# print(str(a))  ## int to str is possible
# print(type(str(a)))

# print(float(a)) ## int to float is possible
# print(bool(a)) ## int to bool is possible
# '''
# except 0,None,'' Flase 
# b=0
# print(bool(b))
# c=None
# print(bool(c))
# d=''
# print(bool(d))
# '''
# print(complex(a)) ## it is possible

# str to other datatypes
s='Hello World'
s1='10'
# print(int(s1))## only meaningfull string can be converted into int
# print(int(s))
print(float(s1)) ## yes but only if it is a meaningfull string with base 10

print(bool(s)) ##yes any string
print(complex(s1))## yes only meaninful

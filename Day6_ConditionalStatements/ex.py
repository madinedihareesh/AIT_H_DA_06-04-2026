'''
condtion:(rule)
simple if
ticket=input('Do you have a ticket')
if ticket=='yes' or ticket=='YES':
    print('Welcome to python session')

if else
# age=int(input('Enter your age: '))
# if age>=18 and age<=105:
#     print('Eligble for vote')
# else:
#     print('Not elsible to vote') 
------- -------- ------- ---------
isRaining=input('Is it raining outside?: ')
if isRaining=='Yes' or isRaining=='yes' or isRaining=='YES':
    print('Please take umbarilla along with you')
else:
    print('have a nice day')
--------  ------- ------ ------
num=9

if num%2==0:
    print(num,'is a even number')
else:
    print(num,'is an odd number')    

elif lader:
person=input('Enter your Name: ')
if person=='Hareesh':
    print('Hareesh is traing students')
elif person=='jyothi':
    print(person,'is learning python')
elif person=='abhi':
    print(person,'is learning python') 
elif person=='siva':
    print(person,'is learning python') 
else:
    print('nobody in the class room') 
------ ------- --------- ------------- 
bill_amount=int(input('Enter your bill amount: '))
if bill_amount>=5000 and bill_amount<100000:
    print('you got 25 persent discount')
    print('you have to pay:',bill_amount-(bill_amount*0.25))
elif bill_amount>=3000 and bill_amount<5000:
    print('you got 15 persent discount')
    print('you have to pay:',bill_amount-(bill_amount*0.15))
elif bill_amount>=2000 and bill_amount<3000:
    print('you got 10 persent discount')
    print('you have to pay:',bill_amount-(bill_amount*0.1))
else:    
    print('sorry, you got no discount you bill is',bill_amount)   
nested conditional statments
marks=int(input('Enter the marks: '))
if marks>=0:
    if marks>=80 and marks<=100:
        print('Grade \'A\'')
    elif marks>=60 and marks<80:
        print('Grade \'B\'')
    elif marks>=50 and marks<60:
        print('Grade \'c\'')  
    elif marks>=40 and marks<50:
        print('Grade \'D\'')
    else:
        print('Grade \'F\'')
else:
    print('Please Enter the marks grater than \'0\'') 
match
day=int(input('Enter your day no: '))

match day:
    case 0:
        print('Sunday')
    case 1:
        print('Mon')
    case 2:
        print('Tus')
    case 3:
        print('wed')
    case 4:
        print('Thrus')
    case 5:
        print('Friday')
    case 6:
        print('sat')                        
    case _:
        print('Enter a valued number from 0-6')

------ -------- ------- ------ ----

flavor=input('Enter your Flavor:')

match flavor:
    case 'venila':
        print(flavor,'is a vailable')
    case 'Redwellwet':
        print(flavor,'is available')
    case 'Blackcurrent':
        print(flavor,'is available')
    case 'Buttrscotch':
        print(flavor,'is available')
    case _:
        print(flavor,'is not available')         
indentation:

syntax created by the creators of python language 
to maintain the block {}
'''

# name=input('Enter your name')
# age=int(input('ENter your age'))

# age=int(input('Enter your age: '))
# if age>=18 and age<=105:
#     print('Eligble for vote')
# else:
#     print('Not elsible to vote')    

                              


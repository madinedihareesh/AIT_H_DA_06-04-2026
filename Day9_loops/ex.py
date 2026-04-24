'''
factors of a number
i=1
num=int(input('Enter a number:'))
count=0
while i<=num:
    if num%i==0:
        print(i,end=' ')
        count+=1
    i+=1 
print('no of factors for',num,'is',count) 

prime number
j=1
while j<=100:
    i=1
    count=0
    while i<=j:
        if j%i==0:
            count+=1
        i+=1
    if count==2:
        print(j,'is a prime number') 
    else:
        print(j,'is not a prime number')  
    j+=1      
print a table 
num=16
i=1
while i<11:
    print(num,'*',i,'=',num*i)
    i+=1        
eval
a=input('Enter a number')
b=input('Enter b number')
res=eval(f'{a}+{b}')
print(res)


*
**
***
****
*****
i=1
while i<6:
    j=1
    while j<6:
        if i>=j:
            print('*',end='')
        j+=1
    print('')
    i+=1 

i=1
while i<6:
    print('* '*i,end='')
    i+=1
    print('') 
- - - - * -
- - - * - *
- - * - * - *
- * - * - * - *
* - * - * - * - *
i=1
while i<6:
    j=1
    while j<i+1:
        print(j,end=' ')
        j+=1
    print('')
    i+=1  

'''

               

 






           


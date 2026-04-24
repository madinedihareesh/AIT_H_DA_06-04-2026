'''
leap year:
year= int(input('Enter the Year: '))
if year%100==0:
    if year%400==0:
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
elif year%4==0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year') 

string='sos'
res=''
for i in range(len(string)-1,-1,-1):
    res+=string[i]
if string==res:
    print(string,'is a palndrome')
else:
    print(string,'is not a palandrome')     
'''
       
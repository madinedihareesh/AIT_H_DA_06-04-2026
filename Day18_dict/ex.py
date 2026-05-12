'''d={'key':'value'}
print(type(d))
d1={1:'one',2:12.59,3:10+9j,4:True,5:[1,2,3,4,5],6:(9,8,7,6,5)}
print(type(d1))
print(d1)
d2={}
print(type(d2))
l1=[1,2,3,4,5]
l2=['one','two','three','four','five']
s=zip(l1,l2)
d3=dict(s)
print(d3)
e=enumerate('python',10)
d4=dict(e)

#read
for i in d1:
    print(d1.get(i))

#write
d1['seven']=7
print(d1) 

d1.update({'eight':8})
print(d1)

d1.update({1:'Ace'})
print(d1)

print(dir(dict))

#methods:
d5=d1.copy()
print(d5);print(d1)
print(id(d5));print(id(d1))

d6=dict.fromkeys([1,2,3,4,5,6])
print(d6)

k=d1.keys()
print(k)

v=d1.values()
print(v)

i=d1.items()
print(i)

d1.pop('eight')
print(d1)

d1.popitem()
print(d1)

d1.clear()
print(d1)'''

# del(d1)
l=[(1,'one'),(2,'two'),(3,'three')]
d1={x:y for x,y in l}
print(d1)

l1=[1,2,3,4,5]
l2=['one','two','three','four','five']

d2={x:y for x,y in zip(l1,l2)}
print(d2)

l3=['john','smith','berry','charlie']
d3={x:y for x,y in enumerate(l3,1)}
print(d3)
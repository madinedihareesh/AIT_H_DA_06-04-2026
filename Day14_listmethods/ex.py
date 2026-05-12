'''
'index' 
'append', 'extend','insert'  ## adding elemnts to a list
'pop','remove'
'sort','reverse',
'copy', 'count'
clear
sum()
min()
max()
del()

'''
l=[1,2,3,4,5,6,7,3]
  
print(l.index(3,l.index(3)+1))

l.append(8)
print(l)

l.extend([9,10,11])
print(l)

l.insert(0,14)
print(l)

l.pop()
print(l)

l.remove(14)
print(l)

l.remove(3)
print(l)

l.remove(3)
print(l)


l1=[90,10,40,30,60,80,50,20,70,100]
l1.sort(reverse=True)
print(l1)

l2=[9,7,5,4,1,2,3]
l2.reverse()
print(l2)


l1=[1,2,3,4,5,6,7]
l2=l1
print(id(l1))
print(id(l2))

l3=l1.copy() ##hallow 
print(l3)
print(id(l1))
print(id(l3))


l1=[1,2,3,4,5,6,3,2]
print(l1.count(3))


print(sum(l1))
print(min(l1))
print(max(l1))


l1.clear()
print(l1)

del(l1)
print(l1)
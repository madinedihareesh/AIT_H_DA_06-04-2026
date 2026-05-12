# t=()
# print(type(t))
# t1=(3,)
# print(type(t1))
# t2=tuple([1,2,3,4,5,6,7]) ##type conversions
# print(type(t2))
# t3=(1,2,3,4,5,6,7)
# print(type(t3))
# t4=1,2,3,4,5,6,7
# print(type(t4))
# names='john','james','bruce','peter'
# print(type(names))

# name1,name2,name3,name4=names
# print(name1,name2,name3,name4)

# t5=(1,12.95,12+9j,True,'Something',1)
# print(type(t5))


# print(dir(tuple))

# '''
# Tuple: is an ordered collection of hetro elements,allows duplicates.
# it is immutable
# '''
# t6=t4[0:4]
# print(t6)

# concatination and repitation is possible or not

# t1=(1,2,3,4)
# t2=(5,6,7,8)
# t3=t1+t2
# print(t3)
# print(id(t1))
# t1*=3
# print(id(t1))

# t1=(1,2,3,4,5)
# for i in t1:
#     print(i)

t1=tuple([x for x in range(1,6)])
print(t1)

t2=(*(x for x in range(1,6)),)
print(t2)

print(sum(t2))
print(min(t2))
print(max(t2))

del(t2)
print(t2)



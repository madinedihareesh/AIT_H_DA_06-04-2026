# s={1,2,3,4,5,6}
# print(type(s))
# s1=set()
# print(type(s1))
# s2={3}
# print(type(s2)) 

# s={1,2,3,1,4,5,6,7,9,8,2,3,'sting',10+11j}
# print(s)
# print(id(s))
# for i in s:
#     print(i)

'''
set is a collection of elements
it is not going to allow dupilicates
it is unordered
it is accepting hetrogenious elements
it is mutable

set is mutable unordered collection of hetro-genious elemnts,dose not allow duplicates
'''  

# print(dir(set))
# s.add(10)
# print(s)
# print(id(s))

# a={1,2,3,4,5}
# b={4,5}

# c=a.union(b)
# print(c)
# d=a.intersection(b)
# print(d)

# e=a.difference(b)
# print(e)
# f=b.difference(a)
# print(f)
# g=a.symmetric_difference(b)
# h=b.symmetric_difference(a)
# print(g)
# print(h)

# a.intersection_update(b)
# a.difference_update(b)
# print(a)
# a.symmetric_difference_update(b)
# print(a)

# a={1,2,3}
# b={4,5,6}
# print(a.isdisjoint(b))

# oparators on sets
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a|b) ##union
# print(a&b) ##intersection
# print(a-b) ##diffrence
# print(a^b) ##sematic diffrence

a={1,2,3,4}
a.add(5)
print(a)
a.update([6,7,8])
print(a)

b=a.copy()
print(id(a),id(b))

b.pop()
print(b)
b.pop()
print(b)

b.clear()
print(b)

# del(b)
# print(b)

s={x for x in range(1,6)}
print(s)
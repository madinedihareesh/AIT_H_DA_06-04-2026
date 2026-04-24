s='AchieversIT' ## string is immutable 
'''# splicing
s1=s[0:9] ## can create a new string from the exsiting string.
# we can not modify the exisitng string. because it is immutable
print(s1)
print(s)
s2=s[0:]
print(s2)
s3=s[:]
print(s3)
s4=s[2:]
print(s4)
s5=s[::2]
print(s5)
s6=s[::-1]
print(s6)'''

# String Methods:
# find
print(s.find('A')) ##first occ
# for i in s:
#     print(s.find(i),'-',i)
print(s.find('e',s.find('e')+1))## second occ
print(s.find('B')) 
print(s.rfind('e')) ## last occ

# index
print(s.index('A'))
# print(s.index('B'))
print(s.rfind('e'))

# ljust('how munch length to add to a string','which char has to replace the existing empty spaces')
print(s.ljust(15,'$'))
# rjust
print(s.rjust(15,'$'))

# center
print(s.center(19,'$'))

# zfill
print(s.zfill(19))

# Strring 
# s1='    AchieversIT    '
# print(len(s1))
# s2=s1.lstrip()
# print(s2)
# print(len(s2))
# s3=s1.rstrip()
# print(s3)
# print(len(s3))
# s4=s1.strip()
# print(s4)
# print(len(s4))

s1='Hi the hello world'
print(s1.split(' '))   

s2=s1.replace('world','universe')
print(s2)
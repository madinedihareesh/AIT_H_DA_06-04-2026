'''
l=[condition for x in rang(1,11)]
'''

# l=[x for x in range(1,11)]
# print(l)
# l1=[x**2 for x in range(1,11)]
# print(l1)
# l2=[x.lower() for x in 'PYTHON']
# print(l2)
# l3=[int(x) for x in '12345']
# print(l3)

'''
10 11 12. 10 11 12
21 22 23. 21 22 23
31 32 33. 31 32 33
'''
l=[1,2,3]
l2=[[1,2,3],[4,5,6],[7,8,9]]
l3=[[9,8,7],[6,5,4],[3,2,1]]

for i in range(0,3):
    for j in range(0,3):
        print(l2[i][j]+l3[i][j],end=' ')
    print()    


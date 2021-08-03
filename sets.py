
'''
a = {1,23,1,4,2,}
b={'ssss','ssss','a','f'}
print(a,'/n',b,type(a))

a=set('aaaaassssfha')
print(a)

d=set([1,2,34,32,32])
print(d)



a =set(range(5))
print(a)

#словари 
a={'itc':'python','bootcamp':'js'}
print(a, type(a))

a=dict(python=1, java=2,c =1)
print()

a=dict.fromkeys(['python','js','c'],100)
print(a)


b={}
a='python the best language'
a = a.split()
b['python']=a[0]
b['является']=a[1]
b['Лучшим']=a[2]
b['языком']=a[3]
print(a)
print(b)


#problema0
dates_of_birth={3,10,11,13,7,31,21,1,10,3,5,6,6}
a=7
dates_of_birth.remove(a)
print(dates_of_birth)

#problem1
farm_1={'dog','cat','mouse','sheep'}
farm_2={'cow','horse','donkey','cat','dog'}
farm_1=farm_2.intersection(farm_1)
print(farm_1)

#problem2
farm_1={'dog','cat','mouse','sheep'}
farm_2={'cow','horse','donkey','cat','dog'}
c=farm_2.difference(farm_1)
print(c)


#Problem3
a={12,33,44,55,66}
a.add(65)
print(a)
a.pop()
print(a)

#problem4
menu={'plov': 120, 'lagman': 150, 'borsh': 100 }
menu['besh_barmak']=130
print(menu)
menu['besh_barmak']=135
print(menu)
menu.pop('borsh')
print(menu)

#problem5
menu={'plov': 120, 'lagman': 150, 'borsh': 100}
drinks=['coca-cola','fanta','sprite']
menu['drinks']=['coca cola','sprite','fanta']
print(menu)
'''
#problem6
metod1={'pink','yellow','black'}
metod2={'pink','white','orange','green'}
#a=metod1.difference(metod2)
metod1.intersection(metod2)
print(metod1)

#problem7


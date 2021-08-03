'''
a=[[1,'gggg'],[2,'zzzz']]
for i in a:
	i[0]=4
	i[1]='ssa'
print(a)	
'''
'''
a=[]
a.append(3)
a.append('hello')
print(a)
'''

'''
#problem1
a=['Nura','Adelya','Estelya','Tahmina','Liza']
b=('Asan','Uson','Oma','Disa')
c=('Musya','Erbol','Inna')
d=('Salavat','Artur','Vika')
e=('Ilona','Luza')
a.append(e)
a.append(d)
a.append(c)
a.append(b)
print(a)
'''
'''
#problem2
names = ('Pepsi','Cola','Fanta')
print(names.index('Cola'))
print(names[2])
print(names[0:3])
'''
'''
#problem3
a=[]
a.append('Nura')
a.append(4)
a.append(4.5)
a.append(('black',))
print(a)
'''
'''
#problem33
names = ['Asan','Mazya','Uson','Oma','Disa']
a =' '
print(a.join(names))
'''
'''
#problem4
city = ['Bishkek','Beijing','New York']
country = ['Russia','China']
a= city+country
print(a)
'''

'''
#problem5
names = ['jack','jimmy','jackson','jhon','jackson','jimmy','jack','jhon','jimmy','jack']
a = 'jack'
print(names.count(a))
'''

'''
#problem6
names = ['jack','jimmy','oskar','jhon','tom','oskar','tom','oskar']
while i==names:
	if i =='oskar':
		names.remove('oskar')
print(names)
'''

'''
#problem7
a=[' ']
d=' Nura '
e=' 1998 '
c=' Python '
x=d + e + c
print(x)
'''

#problem8
pythonList=['int','str','bool','if','else','elif','loop','tuple','list','none','true','None','True','Falce']
print(pythonList.index('loop'))
print(pythonList.pop(6))

'''
#problem11
pythonList=['int','str','bool','if','else','elif','loop','tuple','list','none','true','None','True','Falce']
print(pythonList[1:3])
'''
'''
#problem9
numbers=[123,321,2,543,64,463,234,867,6234,63246,3,43]
a = 123*321*2*543*64*463*234*867*6234*63246*3*43
print(a)
'''

'''
#zadacha1
a=[1,1,2,3,5,8,13,21,34,55,89]
for elem in a:
	if elem>5:
		print(elem)
'''
'''
#zadacha2
digits=(113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for elem in digits:
	if elem/9:
		print(elem/9)
'''
'''
#zadacha3
fruits=('banana','strawberry','apple','orage','limon','ananas')
print(fruits[1 and 5])
'''
'''
#zadacha4
spisok_1=('Lamborgini',17,'4456',2020,'Paris','USA',11,23)
spisok_2=('Ferrari',17,4456,2021,'PARIS','UK',777,23)
spisok_1.extend(spisok_2)
print(spisok_2)
'''
'''
#zadacha5
a=300
b=237
if elem in a:
	if 
'''
'''
#problema10
a='aasd 8585888 aasd'
b=[]
c=[]
for i in a:
		if i.isnumeric():
				b.append(int(i))
		else:
			c.append(i)
			print(b,'\n', c)		
'''			
numbers = ['yellow', 2021,'black', 19, 'why', 'rosie']  
letters = ['red','three',12,11,7]
a=[]
b=[]
*3

#1
lang1='Rust'
languages=['go','java','python','javascript','ruby']
for  i in range(6):
	if languages[i] == lang1:
		print('yes')
	else:
		print('Not')

#2
lang1='php'				
languages=['go','java','python','javascript','ruby']
i=0
while languages [i] !=lang1:
	print(languages[i])	
	i = i+1

#problem3
a=7
for i in range (5):
	print((a*a)*i)

#4
lang1='Rust'
Languages=['go','java','python','javascript','ruby']

#5
for x in range(-9,9):
	print(10-abs(x), end=',')
print (1)


#6
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
i=0
while i<15:
	print(i, names[i])
	i+=2

#7
names=('maksat','lyazat','Daniyar','Aibek','Atai','Salavat','Adinai','Joomart','Alymbek','Ermek','Dastan','Bekmamat','Aslan')
i=2
while i<14:
	print(i, names[i])
	i+=2


#8
a = float(input('Введите число:  ') )
# 1. Это число трёхзначное? 
if a > 99 and a< 999 or a < -99 and a > -999:
	print( "1# трехзначное число")
else:
	print( "1# не трехзначное число")
# 2. Это число положительное и отрицательное?
if  a>0: 
 	print("2# Положительное число")
elif a<0:
        print("2# Отрицательное число")
# 3. Это число делится на 31 без остатка?
if   a // 31:
	print('3# делится без остатка на 31')
else:
	print('3# не делится без остатка на 31')
# 4. Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число
if a > 100 and a // 17 or a > 150 and a==13**2 :
	print('4#', a)
else:
	print('4# не соответствует требованиям')
# 5. Если его умножить на 99 и разделить на 5 и прибавить -9
c = (a*99/5)+(-9)
print('5# Если его умножить на 99 и разделить на 5 и прибавить -9')
print(c)


#9
s = 0
for i in range(-100, 100): 
	if i %13==0 and i %2 ==0:
		s +=1
		print(i**2)
print("end #1")
# 2 . Каждое 7 число проверять на четность и выводить на экран,в случае,если оно нечётное.
d = 0
for r in range(-100, 100, 7):
	if r%2!=0:
 		d += 1
 		print(r)
print('end #1') 
print(s, "значение подходит под первое условие")
print(d, "значение подходит под второе условие")

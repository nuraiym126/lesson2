'''
a = 'Сегодня Кирилл был без настроения'
print('Сегодня Кирилл'.upper(),'был без настроения'.lower())
'''	
'''
#problem1
a = 'yellow'
print(a.isdigit())
'''
'''
#problem2
a = input()
b = 'GitHub'
print(b.split(a))
'''
'''
#problem3
a= 'Ботнет IPStorm, в которой ранее входили лишь Windows-машины, увеличился до 13500 зараженных систем'
print(a.replace('е','3'))
'''
'''
#problem4

a = input('Как вас зовут?')
b = input('Сколько вам лет?')
c = input('Какой ваш любимый фильм?')
print(f'Hello,{a}')
print(f'Отличный выбор,{c}')

#problem5
a = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(a.count(" "))


#problem6
a = 'Самые важные собЫтия в миРе инфосека за сентябрь'
print('|'.join(a))

#problem7
a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(a.title())


'''
i = 0

while i < 20:
	i = i+2
	print(i)
print("конец")
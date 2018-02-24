names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(i)

names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
    print(i, len(i))

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for i in names:
	if is_male[i] == False:
		print(i, 'женский')
	else:
		print(i, 'мужской')

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print('Всего', len(groups), 'группы')
for i in groups:
	print('В группе', len(i), 'ученика')

print('Группа 1:', groups[0], '\nГруппа 2:', groups[1]) #наверно будет замечание, что это слишком в лоб и не универсально
#ниже я нашла функцию, которая дает мне идекс, но наверно тоже можно как то проще сделать...не знаю...
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for indx, i in enumerate (groups, 1):
    print('Группа', indx, ':', i)
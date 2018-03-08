def get_names_frequency(class_list):
    new_dict = {}
    for user_info in class_list:
        name = user_info.get('name')
        if name not in new_dict:
            new_dict[name] = 1
        else:
            new_dict[name] +=1
    return(new_dict)
print(get_names_frequency([{'name': 'Вася'}]))  # {'Вася': 1}
print(get_names_frequency([
    {'name': 'Вася', 'second_name': 'Петров'},
    {'name': 'Вася', 'second_name': 'Васнецов'}
]))  # {'Вася': 2}
print(get_names_frequency([
    {'name': 'Вася'},
    {'name': 'Петя', 'second_name': 'Васнецов'}
]))  # {'Вася': 1, 'Петя': 1}

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша
count_names = {}
for student_names in students:
	name = student_names.get('first_name')
    count_names[name] = count_names.get(name, 0) + 1 
counter = 1
for key in count_names:
    r = count_names[key]
    if r > counter:
        counter = r
        most_common_name = key
print('Самое частое имя среди учеников:', most_common_name)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

for number, student_classes in enumerate(school_students, 1):
	count_names = {}
	for names in student_classes:
		name = names.get('first_name')
        count_names[name] = count_names.get(name, 0) + 1 
		counter = 1
		for key in count_names:
			r = count_names[key]
			if r > counter:
				counter = r
				most_common_name = key
	print('Самое частое имя в классе', number,':', most_common_name)

	# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
result_male_female = {}
a = 1
b = 1
for classes in school:
    students = classes.get('students')
    number_class = classes.get('class')
    new_classes = {}
    for names in students:
        name = names.get('first_name')
        new_classes[name] = is_male.get(name)
    for user_info in new_classes:
        if new_classes[user_info] == False:
            result_male_female['девочки'] = a
            a = a + 1
        else:
            result_male_female['девочки'] = 0
        if new_classes[user_info] == True:
            result_male_female['мальчика'] = b
            b = b + 1
        else:
            result_male_female['мальчика'] = 0
    print('В классе', number_class, result_male_female.get('девочки'), 'девочки и', result_male_female.get('мальчика'), 'мальчика')


		
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a



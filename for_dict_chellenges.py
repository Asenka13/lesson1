# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
	  {'first_name': 'Вася'},
	  {'first_name': 'Петя'},
	  {'first_name': 'Маша'},
	  {'first_name': 'Маша'},
	  {'first_name': 'Петя'},
	]
# ???
	
	# Пример вывода:
	# Вася: 1
	# Маша: 2
	# Петя: 2
frequency_of_names = {}
for student_names in students:
	frequency_of_names[student_names.get('first_name')] = students.count(student_names)
for key in frequency_of_names:
	print(key +':', frequency_of_names[key])



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
    count_names [student_names.get('first_name')] = students.count(student_names)
counter = 1
for key in count_names:
    r = count_names[key]
    if r > counter:
        counter = r
        most_common_name = key
print('Самое частое имя среди учеников:', most_common_name)
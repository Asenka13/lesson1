from collections import Counter
students = [
      {'first_name': 'Вася', 'second_name': 'Пупкин'},
      {'first_name': 'Петя', 'second_name': 'Иванов'},
      {'first_name': 'Маша', 'second_name': 'Петрова'},
      {'first_name': 'Маша', 'second_name': 'Иванова'},
      {'first_name': 'Петя', 'second_name': 'Сидоров'},
    ]
# ???
    
    # Пример вывода:
    # Вася: 1
    # Маша: 2
    # Петя: 2
names_list = []
for student_names in students:
    names_list.append(student_names.get('first_name'))
frequency_names = dict(Counter(names_list))
for name in frequency_names:
    print(name,':', frequency_names[name])
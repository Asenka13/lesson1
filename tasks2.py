students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
first = students.count({'first_name': 'Вася'})
second = students.count({'first_name': 'Маша'})
third = students.count({'first_name': 'Петя'})

print('Вася:', first, '\nМаша:', second, '\nПетя:', third)


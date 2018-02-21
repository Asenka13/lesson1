user_info = {'first_name' : 'Nastya', 'last_name' : 'Boguslavskaya'}
print (user_info.get('first_name'))

user_info = {}.fromkeys (['first_name', 'last_name'])
name = input ('Введите Ваше имя ')
user_info['first_name'] = name
last_name_var = input ('Введите Вашу фамилию ')
user_info['last_name'] = last_name_var
print (user_info)
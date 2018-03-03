def get_names_frequency(class_list):
    new_list = []
    for names in class_list:
    	new_list.append(names.get('name'))
    new_dict = {}
    for name in new_list:
    	try: new_dict[name] += 1
    	except KeyError: new_dict[name] = 1

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
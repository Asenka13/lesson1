# Задание 1
# Сделать так, чтобы функция возвращала результат своей работы

def format_message(message):
    return(message.capitalize() + '!')  # тут надо что-то поменять
    
msg = format_message('hello')  # тут ничего не должно выводиться в консоль
print(msg) # тут должно вывестись 'Hello!'


# Задание 2
# Сделать так, чтобы у функции можно было указывать завершающий знак препинания.

def format_message(words, mark):
	punctuation_mark = '.:,!?'
	for marks in punctuation_mark:
		words = words.replace(marks, '')
	words_with_marks = words + mark
    return(words_with_marks.capitalize())

print(format_message('hello', '!'))  # должно быть Hello!
print(format_message('hello!', '!'))  # тоже должно быть Hello! (не Hello!!)
print(format_message('how are you', '?'))  # должно быть How are you?


# Задание 3
# Сделать так, чтобы если знак не указан, использовался восклицательный знак.

def format_message(words, sign = '!'):
    result = words + sign
    return(result.capitalize())

print(format_message('hello'))  # должно быть Hello!
print(format_message('hello', '!'))  # тоже должно быть Hello!
print(format_message('hello', sign='!'))  # опять должно быть Hello!
print(format_message('how are you', '?'))  # должно быть How are you?


# Задание 4
# Добавить ограничение на длину.
# Если строка выше заданной длины, то она обрезается и в конце ставится троеточие.
# Если заданная длина не указана, то она 100.

def format_message(words, sign = '!', max_length = 100):
    result = words + sign
    if len(result) >= max_length:
    	new_string = result[:max_length] + '...'
    	return(new_string.capitalize())
    else:
    	return(result.capitalize())

print(format_message('hello'))  # должно быть Hello!
print(format_message('hello', max_length=10))  # тоже должно быть Hello!
print(format_message('how are you', sign='?', max_length=5))  # должно быть How a...
print(format_message('how are you', '?', max_length=20))  # должно быть How are you?


# Задание 5
# Добавить аргумент, который выдаёт подробную информацию о сообщении.
# Если он указан, то функция возвращает не строку, а словарь с предзаполненными полями.
# По-умолчанию значение аргумента – False.

def format_message(words, sign = '!', max_length = 100, with_info=False):
	if with_info == False: 
    	result = words + sign
    	if len(result) >= max_length:
    		new_string = result[:max_length] + '...'
    		return(new_string.capitalize())
    	else:
    		return(result.capitalize())
    else:
    	info_message = {'message': words.capitalize(), 'message_length': len(words), 'sing': sign}
    	return(info_message)

print(format_message('hello'))  # должно быть Hello!
print(format_message('hello', with_info=True))  # должно быть {'message': 'Hello', 'message_length': 5, 'sing': '!'}
def get_summ(one, two, delimeter=' '):
    return str.upper (one) + str (delimeter) + str.upper (two)
result = get_summ('Hello', 'world')
print (result)
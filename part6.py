mylist = [2, 3, 4, 5, 6, 7]
print (mylist)

mylist.append("Python")
print (mylist [0])
print (mylist [6])
print (mylist [1:5])
print (len (mylist))

mylist.index(6)

mylist.remove('Python')
print(mylist)

weather = {'city' : 'Москва', 'temperature' : 20, 'wind' : 'восточный'}
print (weather.get ('city'))
weather['temperature'] = 15
print (weather.get ('temperature'))

len (weather)

"country" in weather

weather['date'] = '27.05.2017'

myweather = []
myweather.append({'01.01.2018' : {'temperature' : 20, 'wind' : 'восточный'}})
myweather.append({'02.01.2018' : {'temperature' : 21, 'wind' : 'западный'}})
myweather.append({'03.01.2018' : {'temperature' : 22, 'wind' : 'южный'}})

print(myweather)

mydictionary = {
	"Петя" : {"city" : "Moscow", "temperature" : 15, "wind" : 2 },
	"Ваня": {"city" : "Chelyabinsk", "temperature" : 13, "wind" : 3 },
	"Маша": {"city" : "Tomsk", "temperature" : 10, "wind" : 5 }
	}
name = str (input ("Введите имя: "))

if name == 'Петя':
	print(mydictionary.get("Петя"))
elif name == 'Ваня':
	print(mydictionary.get("Ваня"))
elif name == 'Маша':
	print(mydictionary.get("Маша"))

	#Если ввести несушествующее имя, то у меня ничего не было, просто пусто

# Я не поняла, как использовать такую штуку с условиями:	for key, value in mydictionary.items():......
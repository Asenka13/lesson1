mydictionary = {
	"Петя" : {"city" : "Moscow", "temperature" : 15, "wind" : 2 },
	"Ваня": {"city" : "Chelyabinsk", "temperature" : 13, "wind" : 3 },
	"Маша": {"city" : "Tomsk", "temperature" : 10, "wind" : 5 }
	}
name = (input ("Введите имя: "))
print(mydictionary.get(name))

#Если ввести несушествующее имя, то у меня ничего не было, просто пусто


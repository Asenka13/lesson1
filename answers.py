def get_answer(question, answers):
	return answers.get(question.lower())
result = get_answer(str(input ()), {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"})
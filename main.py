
right_answers = 0

questions = {
	"Ты носишь высокие туфли?": [["Да", "Я хожу в шпильках", "Я не ношу туфли"], "0"],
	"Тебе сколько лет?": ["20"],
	"Какие у тебя волосы?": [["Рыжие", "Как весенняя лазурь", "Черные"], "0"]
}

for i, question in enumerate(questions.keys()):
	new_line_operand = '\n'
	if len(questions[question]) == 2:
		if (input(f"{i+1}. {question}: \n\n{f'{new_line_operand}'.join([f'{ti}. {answer}' for ti, answer in enumerate(questions[question][0])])}\n") == questions[question][1]):
			print("Верно\n")
			right_answers +=1
		else:
			print("Не верно\n")

	else:
		if (input(f"{i}. {question}: ") == questions[question][0]):
			print("Верно!\n")
			right_answers += 1
		else:
			print("Не верно!\n")
print(f"Вы на {int(right_answers/len(questions.keys())*100)}% Ангелина Бочарова")

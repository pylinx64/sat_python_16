import random

print('Привет я Бот123. Задай вопрос.')

while True:
	text = input('Введи слово: ')
	if text.lower() == 'привет':
		print('Бот123 > Ни хао')
		
	elif text.lower() == 'как дела?':
		print('Бот123 > Нормально')
		
	elif text.lower() == 'как погода':
		a = ['солнечно', '+30', 'прохладно']
		bot_text = random.choice(a)	
		print(bot_text)
		
	else:
		print('Бот123 > Я не понял вопроса.')
	
	

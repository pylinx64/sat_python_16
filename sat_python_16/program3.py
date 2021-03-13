import random
import time

loot = ['Машина', 'безнин', 'minecraft', 'кирпич', '40 грн']


while True:
	answer = input('Сыграть еще раз? (да/нет) ')
	if answer == 'да':
		
		win_box = random.choice(loot)
		print('Ваш приз: ')
		print(win_box)
		time.sleep(.3)		# то же самое что и 0.3
	elif answer == 'нет':
		print('# exit game')
		break
	else:
		print('Неправильный ввод')

import random

# подбирает случайное число и сохраняет его
number_random = random.randint(1, 10)

# человек вводит число 
number_player = input('Введите число от 1 до 100: ')

if int(number_player) == number_random:
	print('$$$ WIN $$$')
else:
	print('You proigrali ((')

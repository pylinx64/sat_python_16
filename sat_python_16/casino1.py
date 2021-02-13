import random

print('-----Приветсвую в казино 3 топора---------')
money = input('Введите кол-во $: ')
money =  int(money)

while True:
	print('ваш счет $: ', money)
	# подбирает случайное число и сохраняет его
	number_random = random.randint(1, 10)

	# человек вводит число 
	number_player = input('Введите число от 1 до 100: ')


	if int(number_player) == number_random:
		print('$$$ WIN $$$')
		money = money + 1000

	elif money < 0:
		print('Деняк нет ( ')
		break

	else:
		print('You proigrali ((')
		money = money - 100
	

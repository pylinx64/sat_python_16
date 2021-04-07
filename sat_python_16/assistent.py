import pyttsx3
from datetime import datetime, time, date 
#from time import time as t

# здесь голос
tts=pyttsx3.init()
tts.setProperty('rate', 200)		# скорость 

# создаем свою команду
def tallBots(text):
	tts.say(text)
	print(text)
	tts.runAndWait()

# сам бот
while True:
	text=input('Введите фразу: ')
	if text.lower() == 'привет':
		tallBots('Бот123 > Ни хао')
		
	elif text.lower() == 'как дела?':
		tallBots('Бот123 > Нормально')
	
	elif text.lower() == 'время':
		time_check = datetime.now()
		hour = time_check.hour
		minute = time_check.minute
		tallBots(str(hour) + ':' + str(minute))
		
		
	elif text.lower() == 'дата':
		tallBots('13/12/2021')
		
	
	# все команды перед else
	else:
		tallBots('Бот123 > Я не понял вопроса.')

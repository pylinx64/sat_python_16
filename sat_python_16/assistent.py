import pyttsx3

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
		tallBots('Ни хао')
		
	elif text.lower() == 'как дела?':
		tallBots('Бот123 > Нормально')

	else:
		tallBots('Бот123 > Я не понял вопроса.')
	

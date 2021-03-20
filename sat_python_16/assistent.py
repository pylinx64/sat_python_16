import pyttsx3

# здесь голос
tts=pyttsx3.init()

# создаем свою команду
def tallBots(text):
	tts.say(text)
	print(text)
	tts.runAndWait()

# сам бот
text='итпмпит'
tallBots(text)

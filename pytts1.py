# Import the required module for text 
# to speech conversion 
import pyttsx3
import os
from sys import platform


# The text that you want to convert to audio 
mytext = 'Welcome to Saksham Code Camp! We encourage you to learn coding to try and solve some real world problems.'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 

# create a function
def textToSpeach(mytext):
	# init tts engine
	engine = pyttsx3.init()
	# speak out text
	engine.say(mytext)
	# gracefully exit
	engine.runAndWait()

def textToMp3file(mytext, mp3filname):
	# init tts engine
	engine = pyttsx3.init()
	# check and replace file extension
	mp3filname.replace('.mp3', '')
	# Saving the converted audio in a mp3 file
	engine.save_to_file(mytext,mp3filname + '.mp3')
	# check os / platform
	if platform == "linux" or platform == "linux2":
		# Playing the converted file (linux)
		os.system("plaympeg " + mp3filname + ".mp3")
	elif platform == "win32":
	 	# Windows...
		os.system("start " + mp3filname + ".mp3")
	elif platform == "darwin":
	 	# Mac os...
		pass
	else:
		# other os
		pass
	engine.runAndWait()

textToSpeach(mytext)
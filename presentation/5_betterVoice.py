from gtts import gTTS
import aiy.cloudspeech
import os
import aiy.audio

def sayBetter(text):
    tts = gTTS(text=text, lang='en')
    tts.save('say.mp3')
    os.system('mpg123 say.mp3')

recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()

sayBetter("Listening to your name...")
myName = recognizer.recognize()
if myName:
    sayBetter("Hello " + myName)




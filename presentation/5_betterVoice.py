from gtts import gTTS
from aiy.cloudspeech import CloudSpeechClient
import os

def sayBetter(text):
    tts = gTTS(text=text, lang='en')
    tts.save('say.mp3')
    os.system('mpg123 say.mp3')

client = CloudSpeechClient()


sayBetter("Listening to your name...")
myName = client.recognize()
if myName:
    sayBetter("Hello " + myName)




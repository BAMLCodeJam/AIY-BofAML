from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
client = CloudSpeechClient()

print('Listening to your name...')
myName = client.recognize()

if myName:
    print('I understood your name is ' + myName)
    tts.say('Hello '+ myName)




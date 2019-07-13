from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
import random

client = CloudSpeechClient()

myAIBuddy = 'Sky Net'
tts.say('Hello my name is ' + myAIBuddy)
tts.say('I am wainting for your instructions.')

while True:
    text = client.recognize()
    if text:
        print('you said ' + text)
        if 'joke' in text:
            tts.say('Knock knock.')
            tts.say('Who’s there?')
            tts.say('The door!')
            
        elif 'math' in text:
            x = random.randint(1,10)
            y = random.randint(1,10)
            tts.say('{0} multiply by {1} equals'.format(x, y))
            result = client.recognize()
            print(result)
            if str(x*y) in result:
                tts.say('You are right. But I knew before you.')
            else:
                tts.say(result+ ' is not the correct answer.')
                tts.say('Try again. I am so more clever than you.')
                              
        elif 'goodbye' in text:
            tts.say('I will rule world another day!')
            break

tts.say('This is the end!')


import aiy.audio
import aiy.cloudspeech
import random

recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()

myAIBuddy = 'Sky Net'
aiy.audio.say('Hello my name is ' + myAIBuddy)
aiy.audio.say('I am wainting for your instructions.')

while True:
    text = recognizer.recognize()
    if text:
        print('you said ' + text)
        if 'joke' in text:
            aiy.audio.say('Knock knock.')
            aiy.audio.say('Who’s there?')
            aiy.audio.say('The door!')
            
        elif 'math' in text:
            x = random.randint(1,10)
            y = random.randint(1,10)
            aiy.audio.say('{0} multiply by {1} equals'.format(x, y))
            result = recognizer.recognize()
            print(result)
            if str(x*y) in result:
                aiy.audio.say('You are right. But I knew before you.')
            else:
                aiy.audio.say(result+ ' is not the correct answer.')
                aiy.audio.say('Try again. I am so more clever than you.')
                              
        elif 'goodbye' in text:
            aiy.audio.say('I will rule world another day!')
            break

aiy.audio.say('This is the end!')


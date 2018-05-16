import aiy.audio
import aiy.cloudspeech

recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()

print('Listening to your name...')
myName = recognizer.recognize()
print('I understood your name is ' + myName)

aiy.audio.say('Hello '+ myName)




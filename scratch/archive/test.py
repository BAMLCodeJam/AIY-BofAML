import aiy.cloudspeech
import aiy.voicehat
import aiy.audio
myButton = aiy.voicehat.get_button()

recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()
aiy.audio.say('Hello my name is ')
while True:
    myButton.wait_for_press()
    print('This is tickling')




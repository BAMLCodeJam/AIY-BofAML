import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

myButton = aiy.voicehat.get_button()

while True:
    myButton.wait_for_press()
    aiy.audio.say('This is tickling')




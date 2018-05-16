import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

led = aiy.voicehat.get_led()
led.set_state(aiy.voicehat.LED.ON)

recognizer = aiy.cloudspeech.get_recognizer()

aiy.audio.say('Listening...')
aiy.audio.get_recorder().start()

while True:
    text = recognizer.recognize()
    if text and 'blink' in text:
        led.set_state(aiy.voicehat.LED.BLINK)
    else:
        print(text)
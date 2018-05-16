import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import scratch
import time
import random

s = scratch.Scratch(host='0.0.0.0')

def on_button_pressed():
    choice = random.choice(('left', 'right', 'up', 'down'))
    print ('%.2f - Move: %s' %(time.time(), choice))
    s.broadcast(choice)
    
recognizer = aiy.cloudspeech.get_recognizer()
aiy.voicehat.get_button().on_press(on_button_pressed)
            
def listen():
    while True:
        try:
            val = s.receive()
            #print ('%.2f - Received: %s' % (time.time(), val))
            yield val
        except Exception as e:
            # scratch.ScratchError:
            raise StopIteration


for msg in listen():
    if 'light' in msg['sensor-update']:
        led = aiy.voicehat.get_led()
        lightOn = msg['sensor-update']['light']
        print('%.2f - Decoded: LED = %s' % (time.time(), lightOn))
        if lightOn == 'True':
            led.set_state(aiy.voicehat.LED.ON)
        else:
            led.set_state(aiy.voicehat.LED.OFF)
    if 'voice' in msg['sensor-update']:
        voice = lightOn = msg['sensor-update']['voice']
        aiy.audio.say(voice)
        print('I just said {0}'.format(voice))
    print(msg['sensor-update'])

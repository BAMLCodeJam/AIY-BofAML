from glob import glob
from contextlib import contextmanager
from pydobot import Dobot
import aiy.audio
import aiy.cloudspeech

@contextmanager
def getDevice():
    available_ports = glob('/dev/*USB*')  # mask for OSX Dobot port
    if len(available_ports) == 0:
        print('no port found for Dobot Magician')
        exit(1)
    device = Dobot(port=available_ports[0], verbose=True)
    device.speed(200)
    yield device
    device.close()

def moveLeft(size=40):
    aiy.audio.say('Going left')
    with getDevice() as device:
        device.go(device.x, device.y-size, device.z)

def moveRight(size=40):
    aiy.audio.say('Going right')
    with getDevice() as device:
        device.go(device.x, device.y+size, device.z)

print('Waiting ...')
recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()
while True:
    text = recognizer.recognize()
    if text:
        if 'left' in text:
            moveLeft(40)
        if 'right' in text:
            moveRight(40)

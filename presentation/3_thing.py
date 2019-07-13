from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
from aiy.board import Board, Led

board = Board()
led = board.led
led.state=Led.ON

client = CloudSpeechClient()

tts.say('Listening...')

while True:
    text = client.recognize()
    if text and 'blink' in text:
        led.state=Led.PULSE_QUICK
    else:
        print(text)
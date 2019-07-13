from aiy.voice import tts
from aiy.board import Board

myButton = Board().button

while True:
    myButton.wait_for_press()
    tts.say('This is tickling')




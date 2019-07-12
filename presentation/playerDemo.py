import aiy.audio
import aiy.cloudspeech
import random
from player import Youtube_mp3

recognizer = aiy.cloudspeech.get_recognizer()
aiy.audio.get_recorder().start()

myAIBuddy = 'Sky Net'
aiy.audio.say('Hello my name is ' + myAIBuddy)
aiy.audio.say('I am wainting for your instructions.')

while True:
    text = recognizer.recognize()
    if text:
        print('you said ' + text)
        if 'play song' in text or 'Play song' in text:
            aiy.audio.say('What should I play')
            textPlay = recognizer.recognize()
            if textPlay:
                aiy.audio.say('Ok, I will play '+textPlay)
                youtube = Youtube_mp3()
                youtube.url_search(textPlay, 1)
                player = youtube.play_media(1)
                player.play()
                aiy.audio.say('Tell me to stop')
                while True:
                    command = recognizer.recognize()
                    print(command)
                    if command and (command == 'stop' or command == 'Stop'):
                        player.stop()
                        aiy.audio.say('Goodbye')
                        aiy.audio.say('I will rule world another day!')
                        break
                break
        elif 'goodbye' in text:
            aiy.audio.say('I will rule world another day!')
            break
aiy.audio.say('This is the end!')



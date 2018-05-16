#!/usr/bin/env python3

import json
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import aiy.cloudspeech
import aiy.voicehat
import sys
from gtts import gTTS
import os
import threading
from select import select

PORT = 9000

class ButtonThread(threading.Thread):
    def __init__(self, server):
        super().__init__()
        self._stopEvent = threading.Event()
        self._aiButton = aiy.voicehat.get_button()
        self._server = server
        
    def stop(self):
        self._stopEvent.set()
        
    def stopped(self):
        return self._stopEvent.is_set()
    
    def run(self):
        print('Starting AI button trigger.')
        while(not self.stopped()):
            self._aiButton.wait_for_press()
            print('Button pressed')
            #here dispatch to all opened connected socket
            for ready in self._server.listeners:
                if ready != self._server.serversocket:
                    if ready in self._server.connections:
                        client = self._server.connections[ready]
                        client.inputCallback('onButton', True)
            
# This class inherits from WebSocket.
# It receives messages from the Scratch and interact with the AI box
class S2Pi(WebSocket):
    
    def __init__(self, server, sock, address):
        super().__init__(server, sock, address)
        self._led = aiy.voicehat.get_led()
        self._led.set_state(aiy.voicehat.LED.OFF)
        
    def handleMessage(self):
        # get command from Scratch2
        payload = json.loads(self.data)
        print('Payload received {0}'.format(payload))
        client_cmd = payload['command']
        print(client_cmd)
        if client_cmd == 'turnOn':
            self._led.set_state(aiy.voicehat.LED.ON)
        elif client_cmd == 'turnOff':
            self._led.set_state(aiy.voicehat.LED.OFF)
        elif client_cmd == 'say':
            textToSay = payload['text']
            self.sayBetter(textToSay)
        elif client_cmd == 'sayLang':
            textToSay = payload['text']
            lang = payload['lang']
            self.sayBetter(textToSay, lang)
        elif client_cmd == 'recognise':
            textToRecognise = payload['text']
            self.recognise(textToRecognise)
        elif client_cmd == 'ready':
            self.sayBetter('I am now connected to Scratch.')
        else:
            print("Unknown command received", client_cmd)
    
    def sayBetter(self, text, lang = 'en'):
        tts = gTTS(text=text, lang=lang)
        tts.save('say.mp3')
        os.system('mpg123 say.mp3')
        
    def recognise(self, text):
        self.sayBetter('Listening')
        recognizer = aiy.cloudspeech.get_recognizer()
        aiy.audio.get_recorder().start()
        capturedText = recognizer.recognize()
        print(capturedText)
        recognised = False
        if capturedText:
            self.sayBetter(capturedText)
            if capturedText == text:
                recognised = True
            else:
                self.sayBetter('Sorry, I recognised %s instead of %s' % (capturedText, text))
        self.sayBetter('Sorry, I did not recognize this')
        msg = json.dumps({'Recognised': recognised})
        self.sendMessage('True')
    
    # send info back up to scratch
    def inputCallback(self, callBackCategory, callBackValue):
        msg = json.dumps({callBackCategory: callBackValue})
        self.sendMessage(msg)
        print('callback', msg)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def runServer():
    print('extension is {0}'.format('/home/pi/AIY-BofAML/scratch/baml_ext.js'))
    server = SimpleWebSocketServer('', PORT, S2Pi)
    buttonTrigger = ButtonThread(server)
    buttonTrigger.start()
    print('Server listening on port {0}'.format(PORT))
    server.serveforever()
    
if __name__ == "__main__":
    try:
        runServer()
    except KeyboardInterrupt:
        sys.exit(0)
#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A small QA game with different categories."""
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
from aiy.board import Board, Led
import random


def game_questions():
    return {
        'Maths': [
                ('What is 7 + 8?',                                      15),
                ('How many days are in a week?',                        7),
                ('What is 56 divided by 7?',                            8),
                ('What is 4 multiplied by 3?',                          12),
                ('How many minutes are in three hours and a half?',     210),
                ('What shape has 3 sides?',                             'triangle'),
                ('How many legs 4 ducks and 2 cows have altogheter?',   16),
                ('What is the square root of 16?',                      4),
                ('Calculate 2 with an exponent of 3!',                  8)
        ],
       'Geography': [
            ('What is the capital of France?',                          'Paris.'),
        ]
    }


def train_recognizer(recognizer, category):
    recognizer.recognize(hint_phrases=category)
    questions_and_answers = game_questions()[category]
    for question, answer in questions_and_answers:
        recognizer.expect_phrase(question)
        recognizer.expect_phrase(str(answer) if isinstance(answer, int) else answer)



def main():
    recognizerGame = CloudSpeechClient()
    recognizer = CloudSpeechClient()

    board = Board()
    button = board.button
    led = board.led
    train_recognizer(recognizer, 'Maths')
    
    game_categories = game_questions().keys()
    total_score = 0

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize(hint_phrases=['game', 'play'])

        if not text:
            print('Sorry, I did not hear you.')
            tts.say('Sorry, I did not hear you.')

        else:
            print('You said "', text, '"')
            if 'a game' in text:
                led.state=Led.ON
                tts.say('Welcome to do greatest game ever! The available categories are: {0}. Press the button and pick one!'.format(', '.join(game_categories)))
                button.wait_for_press()
                print('Listening for game...')
                game = recognizerGame.recognize(hint_phrases=['Maths', 'Geography'])
                print(game)
                if not game:
                    print('Sorry, Game I did not hear you.')
                    tts.say('Sorry, Game I did not hear you.')
                elif 'Maths' in game:
                    led.state = Led.ON
                    tts.say('Get ready for your Maths questions! Once you have the answer, press the button and speak.')
                    questions_and_answers = dict(game_questions()['Maths'])
                    questions = questions_and_answers.keys()
                    random.shuffle(questions)

                    for question in questions[:5]:  # first 5 questions after randomly shuffling
                        tts.say(question)
                        led.state = Led.OFF

                        print('Press the button and speak')
                        button.wait_for_press()
                        recorded_text = recognizer.recognize()
                        answer = questions_and_answers[question]
                        if answer in recorded_text:
                            led.state=Led.ON
                            tts.say('Well done! %s is the correct answer! You score one point!', answer)
                            total_score += 1
                        elif answer not in answer:
                            tts.say('Sorry, the answer I was looking for is %s. No points for you this time!', answer)

                elif 'Geography' in game:
                    return

            elif 'score' in text:
                if total_score > 0:
                    tts.say('Your have scored %s points. Well done!', total_score)
                else:
                    tts.say('So sad, your score is %s points. Don\'t give up!', total_score)

            elif 'goodbye' in text:
                break


if __name__ == '__main__':
    main()
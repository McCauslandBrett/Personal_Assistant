#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:06:58 2019
Resources: https://youtu.be/K_WbsFrPUCk
           https://youtu.be/LFXsG7fueyk
           
           Bird, Steven, Edward Loper and Ewan Klein (2009),
           Natural Language Processing with Python. 
           O’Reilly Media Inc.
           
@author: brett
"""

import speech_recognition as sr
import nltk 
#nltk.download()
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')
r = sr.Recognizer()
r.energy_threshold = 4000
text=""
with sr.Microphone() as source:
    #audio_activate = r.listen_in_background(source)

    print('speak Anything: ')
    audio = r.listen(source)

    #audio = r.listen_in_background(source)
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Sorry I didnt Catch that')
words = nltk.word_tokenize(text)
tagged = nltk.pos_tag(words)
namedEnt = nltk.ne_chunk(tagged)
namedEnt.draw()



def make_appointment():
    return 0
file = open("reminders.txt", "w")

file.write("Reminder:\n")
file.write("Date:\t" + "\n")
file.write("Time:\t" + "\n")
file.write("Location:\t" + "\n")
file.write("With:\t" + "\n")
file.write("\n")
file.close()

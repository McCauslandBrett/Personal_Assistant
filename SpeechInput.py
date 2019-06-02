#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:06:58 2019
Resources: https://youtu.be/K_WbsFrPUCk
           https://youtu.be/LFXsG7fueyk
           
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
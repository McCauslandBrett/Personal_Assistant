#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:43:25 2019

@author: brett
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:06:58 2019
Resources: https://youtu.be/K_WbsFrPUCk
           https://youtu.be/LFXsG7fueyk
           https://www.nltk.org/book/ch08.html
@author: brett
"""

import speech_recognition as sr
import nltk 
import random
import datetime
import pyttsx3


from nltk.corpus import treebank
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 90)
now = datetime.datetime.now()


#nltk.download()
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')

def Reminder(named_ents,_return):
    
    engine.runAndWait()
    found = False
    time= None
    day = None
    for tup in named_ents:
        if tup[0] == 'remind' or tup[0]== 'remember':
            named_ents.remove(tup)
            found == True
        if tup[1]=='CD':
            time = tup[0]
        if tup[0] == 'tomorrow':
            day = tup[0]
        
    if found:
        engine.say('Okay I will set a reminder for you')
    return _return 
        


r = sr.Recognizer()

r.energy_threshold = 4000
text="remind me to take my medicine at 12"

words = nltk.word_tokenize(text)
tagged = nltk.pos_tag(words)
namedEnt = nltk.ne_chunk(tagged)
Reminder(namedEnt)


 
 
 
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
# Dependicies
import speech_recognition as sr
import nltk 
import random
import datetime
import pyttsx3


from nltk.corpus import treebank

# Globels
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 90)
now = datetime.datetime.now()
pattern = 'NP: {<DT>?<JJ>*<NN>}'
r = sr.Recognizer()
r.energy_threshold = 4000

#Downloads

#nltk.download()
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')


text=""

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

def make_appointment():
    return 0

def exportReminder():
    
    file.write("Time:\t" + "\n")
    file.write("Location:\t" + "\n")
    file.write("With:\t" + "\n")
    file.write("\n")
    file.close()

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
        #more specific based on VB
    return _return 

# --- Main ---
def main():

 run = True
 while(run):
    with sr.Microphone() as source:
    #audio_activate = r.listen_in_background(source)
        print('speak Anything: ')
        audio = r.listen(source)

    #audio = r.listen_in_background(source)
        try:
            text = r.recognize_google(audio)
           
            #--- nltk implementation ---
            #print('You said : {}'.format(text))
            #words = nltk.word_tokenize(text)
            #tagged = nltk.pos_tag(words)
            #namedEnt = nltk.ne_chunk(tagged)
            #-------------------------------
            
            #--- spacy implementation ---
            sent = preprocess(text)
            pattern = 'NP: {<DT>?<JJ>*<NN>}'

            cp = nltk.RegexpParser(pattern)
            cs = cp.parse(sent)
            print(cs)

            NPChunker = nltk.RegexpParser(pattern)
            result = NPChunker.parse(sent)
            #result.draw()

            iob_tagged = tree2conlltags(cs)
            pprint(iob_tagged)

            #nlp = spacy.load("en_core_web_sm")
            nlp = en_core_web_sm.load()

            doc = nlp(speech)
            pprint([(X.text, X.label_) for X in doc.ents])


            
        except:
            print('Sorry I didnt Catch that')

    run = False









# testing 
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

NPChunker = nltk.RegexpParser(pattern)
result = NPChunker.parse(sent)
#result.draw()


iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

#nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()

doc = nlp(speech)
pprint([(X.text, X.label_) for X in doc.ents])



#if __name__ == '__main__' :
#   main()



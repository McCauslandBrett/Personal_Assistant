#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:14:41 2019

@author: brett
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:06:58 2019
Resources: https://youtu.be/K_WbsFrPUCk
           https://youtu.be/LFXsG7fueyk
           
           Bird, Steven, Edward Loper and Ewan Klein (2009),
           Natural Language Processing with Python. 
           O’Reilly Media Inc.
           
@author: Tarique & Brett
"""
# Dependicies
import speech_recognition as sr
import nltk 
import random
import datetime
import pyttsx3
import spacy

from pprint import pprint
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Globels

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 100)
now = datetime.datetime.now()

pattern = 'NP: {<DT>?<JJ>*<NN>}'
r = sr.Recognizer()
r.energy_threshold = 4000
cp = nltk.RegexpParser(pattern)
NPChunker = nltk.RegexpParser(pattern)

            #result.draw()




#Downloads
nlp = spacy.load("en_core_web_sm")
#nlp = en_core_web_sm.load()
#nltk.download()
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')




def testing():

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

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

def entityExtraction(doc):
    
    dct ={}
    for x in doc.ents:
        if x.label == 'ORG':
            dct['ORG'] =  x.text
        elif x.label_ == 'GPE':
            dct['GPE'] =  x.text
        elif x.label_ == 'DATE':
            dct['DATE'] = x.text
        elif x.label_ == 'PERSON':
            dct['PERSON'] =  x.text
        elif x.label_ == 'CARDINAL':
            dct['CARDINAL'] = x.text
    return dct
def actionExtraction(sent):
    
    #VB NN 
  
    verb = None
    Noun = None
    for x in sent:
        if  x[1] =='VB'  and verb == None:
            if x[0]== 'set' or x[0]== 'remind':
                verb = x[0]
            if x[0]== 'make':
                verb = x[0]
        if x[1] == 'NN' and Noun == None and verb != None:
            Noun = x[0]
    return(verb,Noun)

#def exportReminder(lst):
   


def Response(action, dct):
    
    engine.runAndWait()
    if action[1] == 'alarm':
        resp = 'Okay I will set a alarm for you'
        if 'DATE' in dct:
            resp += ' for ' + dct['DATE']
            if 'CARDINAL' in dct:
                resp += 'at' + dct['CARDINAL']
        elif 'CARDINAL' in dct:
                resp += 'for' + dct['CARDINAL']
        engine.say(resp)
        
    elif action[1] == 'remind' or action[1] == 'set':
        first = False
        if action[1] == 'set':
            resp = 'Okay I will set a '
            if action[0] != None:
                resp += action[0]
            first = True
        else:
             resp = 'Okay I will set a reminder '
        if action[0] != None:
            resp += 'for ' + action[0]
            first = True
        if 'DATE' in dct:
            if first:
                resp += 'for ' + dct['DATE']
            else:
                resp += 'at ' + dct['DATE']
        if 'CARDINAL' in dct:
            resp += 'at ' + dct['CARDINAL']
        if 'PERSON' in dct:
            resp += 'with ' + dct['PERSON']
        if 'GPE' in dct:
            resp += 'at ' + dct['GPE']
        print('speak')
        engine.say(resp)
        
        
        
        #more specific based on VB
  

# --- Main ---
def main():

 run = True
 text=""
 while(run):
    with sr.Microphone() as source:
    #audio_activate = r.listen_in_background(source)
        print('speak Anything: ')
        audio = r.listen(source)

    #audio = r.listen_in_background(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('Sorry I didnt Catch that')
            continue
    #--- nltk implementation ---
        #print('You said : {}'.format(text))
        #words = nltk.word_tokenize(text)
        #tagged = nltk.pos_tag(words)
        #namedEnt = nltk.ne_chunk(tagged)
        #-------------------------------
            
        #--- spacy implementation ---
        sent = preprocess(text)
        print('sent', sent)
        result = NPChunker.parse(sent)
        print('result',result)
        action = actionExtraction(sent)
        print('actionExtraction: ',action)
       
        cs = cp.parse(sent)
        iob_tagged = tree2conlltags(cs)
        #pprint(iob_tagged)
        
        

        doc = nlp(text)
        pprint([(X.text, X.label_) for X in doc.ents])
        dct = entityExtraction(doc)
        Response(action, dct)
        dct.clear()
        text = ''
        #actionExtraction(doc)
        #print(lst)
    run = False









if __name__ == '__main__' :
   main()



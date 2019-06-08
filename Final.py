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

from enum import Enum

class Grm():
    NN = None
    VB = None

# ---action tuple---
# verb =0
# noun =1

alarmcnt = 0
# Globels
verb_terminals_alarm = ['set','make']
noun_terminals_alarm = ['alarm']

verb_terminals_reminder = ['remind','make','set']
noun_terminals_reminder = ['reminder']
#  in verb reminder and not in verb schedule or  noun in noun reminder

verb_terminals_schedule = ['make','set','schedule']
noun_terminals_schedule = ['appointment','meeting','schedule']

#  in verb schedule and not in verb reminder or  noun in noun schedule


verb_terminals = ['set','make','remind','schedule'] 
noun_terminals = ['alarm','reminder','appointment','meeting','schedule']

 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 0.9)  
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
        print(x)
        if x.label_ == 'ORG':
            dct['ORG'] =  x.text
        elif x.label_ == 'GPE':
            dct['GPE'] =  x.text
        elif x.label_ == 'DATE':
            dct['DATE'] = x.text
        elif x.label_ == 'PERSON':
            dct['PERSON'] =  x.text
        elif x.label_ == 'CARDINAL':
            dct['CARDINAL'] = x.text
        elif x.label_ == 'TIME':
            dct['TIME'] = x.text
    print('dictionary: ',dct)
    return dct
def actionExtraction(sent):
    
    #VB NN 
    tm = Grm()
    for x in sent:
        if  x[1] =='VB'  and tm.VB == None: # havent already selected a verb
            if x[0] in verb_terminals: 
                tm.VB = x[0]
        if x[1] == 'NN' and tm.NN == None and tm.VB  != None:
           tm.NN = x[0]
    # just get any verb or noun that comes first in terminal set
    if tm.NN == None and tm.VB== None:
        if  x[1] =='VB' and x[0] in verb_terminals:
            tm.VB = x[0]
        if  x[1] =='NN' and x[0] in noun_terminals:
            tm.NN= x[0]
    return(tm)

#def exportReminder(lst):
   
def testingResp():
    action = ('remind', 'appointment')
    dct = {}
    dct['CARDINAL'] ='5'
   # Response(action,dct)     

def save_to_file(ST, dct):
   
    if ST.NN in noun_terminals_alarm:
        engine.runAndWait()
        engine.say("okay I have set an alarm for you")
        f = open("alarm", "a")
        f.write('Alarm:' + '\n')
        if 'CARDINAL' in dct:
            f.write('CARDINAL: ' +  dct['CARDINAL']+ "\n")
        if 'DATE' in dct:
            f.write('DATE: ' + dct['DATE']+ "\n") 
        if 'TIME' in dct:
            f.write('TIME: ' + dct['TIME']+ "\n") 
        f.write("\n")
        f.close()
     # Identify reminder by verbs 
     #  remind me to 
     # OR Identify reminder by NN 
     #  set a reminder
     
    elif(ST.NN in noun_terminals_reminder 
          or (ST.VB in verb_terminals_reminder and 
              ST.VB not in verb_terminals_schedule)):
          print('okay I will make that reminder for you')
          engine.runAndWait()
          engine.say("okay I will make that reminder for you")
          f = open("remind", "a")
          f.write('Reminder:'+ "\n")
          if 'CARDINAL' in dct:
              f.write('CARDINAL: ' + dct['CARDINAL']+ "\n")
          if 'DATE' in dct:
            f.write('DATE: '+dct['DATE']+ "\n")
          if 'PERSON' in dct:
            f.write('PERSON: ' + dct['PERSON']+ "\n")
          if 'ORG' in dct:
            f.write('ORG: ' + dct['ORG'] + "\n")
          if 'GPE' in dct:
            f.write('GPE: '+ dct['GPE'] + "\n")
          if 'TIME' in dct:
            f.write('TIME: ' + dct['TIME']+ "\n") 
          f.write("\n")
          f.close() 
        # time, date , who | org, 
    elif (ST.NN in noun_terminals_schedule 
          or (ST.VB in verb_terminals_schedule and 
              ST.VB not in verb_terminals_reminder)):
          f = open("appointment", "a")
          engine.runAndWait()
          engine.say("okay I have addded this to your schedule")
          f.write('Appointment:'+ "\n")
          if 'CARDINAL' in dct:
              f.write('CARDINAL: ' + dct['CARDINAL']+ "\n")
          if 'DATE' in dct:
            f.write('DATE: '+dct['DATE']+ "\n")
          if 'PERSON' in dct:
            f.write('PERSON: ' + dct['PERSON']+ "\n")
          if 'ORG' in dct:
            f.write('ORG: '+dct['ORG']+ "\n")
          if 'GPE' in dct:
            f.write('GPE: '+dct['GPE']+ "\n")
          if 'TIME' in dct:
            f.write('TIME: ' + dct['TIME']+ "\n") 
          f.write("\n")
          f.close() 
       
# --- Main ---
def main():

 run = True
 text=""
 #engine.runAndWait()
 while(run):
    with sr.Microphone() as source:
        engine.say('Go ahead I am listning ')
        engine.runAndWait()
        print("say anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print('Sorry I didnt Catch that')
            engine.say('Sorry I didnt catch that')
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
        ST = actionExtraction(sent)
        print('VB: ', ST.VB)
        print('NN: ', ST.NN)
        #print('actionExtraction: ',ST)
        doc = nlp(text)
        pprint([(X.text, X.label_) for X in doc.ents])
        dct = entityExtraction(doc)
        #Response2(ST, dct)
        save_to_file(ST, dct)
        dct.clear()
        text = ''
    run = False

engine.stop()







if __name__ == '__main__' :
  main()
#testingResp()
engine.runAndWait()
engine.say("hello")
#resp=''









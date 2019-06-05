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
from nltk.corpus import treebank

#nltk.download()
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')
r = sr.Recognizer()
r.energy_threshold = 4000
text="remind me to take my medicine at 12"

words = nltk.word_tokenize(text)
tagged = nltk.pos_tag(words)
namedEnt = nltk.ne_chunk(tagged)
namedEnt.draw()

""" Making your own grammar """

groucho_grammar = nltk.CFG.fromstring("""
... S -> NP VP
... PP -> P NP
... NP -> Det N | Det N PP | 'I'
... VP -> V NP | VP PP
... Det -> 'an' | 'my'
... N -> 'elephant' | 'pajamas'
... V -> 'shot'
... P -> 'in'
... """)
 
 
 
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
try:
    parser = nltk.ChartParser(groucho_grammar)
    for tree in parser.parse(sent):
        print(tree)
except:
    print("not in my defined capabilities")
 
 
 
 
 
 
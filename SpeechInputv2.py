#sources: https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import speech_recognition as sr
import copy


sentence = ""

r = sr.Recognizer()
r.energy_threshold = 4000
speech = ""
with sr.Microphone() as source:
    # audio_activate = r.listen_in_background(source)

    print('speak Anything: ')
    audio = r.listen(source)

    # audio = r.listen_in_background(source)
    try:
        speech = r.recognize_google(audio)
        print('You said : {}'.format(speech))
    except:
        print('Sorry I didnt Catch that')

# trying to make a parse tree
sentence = speech
ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))
print(ne_tree)

ex = speech
print(speech)

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)


pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)

NPChunker = nltk.RegexpParser(pattern)
result = NPChunker.parse(sent)
#result.draw()


iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

nlp = spacy.load("en_core_web_sm")
#nlp = en_core_web_sm.load()

doc = nlp(speech)
pprint([(X.text, X.label_) for X in doc.ents])



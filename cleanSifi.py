import re
import random

dictionary_dir = "dictionaries/"

f = open(dictionary_dir + "/internet_archive_scifi_v3.txt")

lines = f.readlines()

sentences = set()
words = set()
sentencesPerProperNouns = {}
sentencesPerWord = {}

MIN_SENTENCE_WORD_COUNT = 3
MAX_SENTENCE_WORD_COUNT = 64
MAX_SENTENCE_COUNT = 300000
MIN_WORD_PREVELANCE = 10
MIN_PN_WORD_PREVELANCE = 200

lines = re.split('[.!?]+', lines[0])

print("working on ", len(lines), "lines")

i=0
for line in lines:

    if i % 100000 == 0:
        print("processed",i,"lines and", len(sentences),"sentences")
    i = i + 1

    sentence = line.strip()
    

    if len(re.findall('[0-9]+', sentence)):
        #has numbers. Just pick another one.
        continue
    
    sentence = re.sub(r'[^a-zA-Z ]', '', sentence.strip())
    while "  " in sentence:
        sentence = sentence.replace("  ", " ")
    
    sentence = sentence.strip()
    
    if len(sentence) <= 0:
        continue
    
    words_ = sentence.split(" ")
    
    if len(words_) < MIN_SENTENCE_WORD_COUNT or len(words_) > MAX_SENTENCE_WORD_COUNT:
        #too long or too short. pass
        continue
    
    for word_i in range(len(words_)):
        #words.add(word)
        word = words_[word_i]
        
        if  word.isupper():
            #its an acronym. pass
            continue
        
        if word[0].islower() and any(map(str.isupper, word)):
            #I don't know what the hell this is. pass
            continue
            
        if word[0].isupper():
            word = word.lower()
            if word not in sentencesPerProperNouns.keys():
                sentencesPerProperNouns[word] = set()
    
            sentencesPerProperNouns[word].add(sentence)
        
        else:
            word = word.lower()
            
            if word not in sentencesPerWord.keys():
                sentencesPerWord[word] = set()
                
            sentencesPerWord[word].add(sentence)
            #words.add(word.lower())
    
    sentences.add(sentence.lower())
    


wordsLeftOut = 0
for word in sentencesPerWord.keys():
    if len(sentencesPerWord[word]) >= MIN_WORD_PREVELANCE and word not in words:
        words.add(word)
    elif word not in words:
        wordsLeftOut = wordsLeftOut + 1

pnWordsLeftOut = 0
for word in sentencesPerProperNouns.keys():

    if len(sentencesPerProperNouns[word]) >= MIN_PN_WORD_PREVELANCE and word not in words:
        words.add(word)
        #print(word, len(sentencesPerProperNouns[word]))
    elif word not in words:
        pnWordsLeftOut = pnWordsLeftOut + 1

words = list(words)
words.sort()

print(len(sentences), "sentences and", len(words), "words with",wordsLeftOut,"+",pnWordsLeftOut,"=",wordsLeftOut+pnWordsLeftOut, "words left out and",  len(lines), "lines")

sentences = list(sentences)
random.shuffle(sentences)
sentences = sentences[:MAX_SENTENCE_COUNT]

f = open(dictionary_dir + "sci_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "sci_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()



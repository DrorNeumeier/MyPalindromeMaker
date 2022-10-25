import re
import random

dictionary_dir = "dictionaries/"
MAX_SENTENCE_COUNT = 300000
MIN_WORD_PREVELANCE = 10

f = open(dictionary_dir + "wikisent2.txt")

lines = f.readlines()

random.shuffle(lines)

sentences = set()
words = set()
sentencesPerWord = {}

for line in lines:
    if len(re.findall('[0-9]+', line)):
        #has numbers. Just pick another one.
        continue
        
    sentence = re.sub(r'[^a-z ]', '', line.strip().lower())
    sentences.add(sentence)
    
    words_ = sentence.split(" ")
    for word in words_:
        #words.add(word)
        
        if word not in sentencesPerWord.keys():
            sentencesPerWord[word] = set()
            
        sentencesPerWord[word].add(sentence)

    if len(sentences) >= MAX_SENTENCE_COUNT:
        break

for word in sentencesPerWord.keys():
    if len(sentencesPerWord[word]) >= MIN_WORD_PREVELANCE:
        words.add(word)

words = list(words)
words.sort()

f = open(dictionary_dir + "wiki_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "wiki_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()

    

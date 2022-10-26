import re
import random

dictionary_dir = "dictionaries/"

f = open(dictionary_dir + "/internet_archive_scifi_v3.txt")

lines = f.readlines()

sentences = set()
words = set()
sentencesPerWord = {}

MIN_SENTENCE_WORD_COUNT = 3
MAX_SENTENCE_WORD_COUNT = 64
MAX_SENTENCE_COUNT = 300000
MIN_WORD_PREVELANCE = 10

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
    if len(words_) > MAX_SENTENCE_WORD_COUNT or len(words_) < MIN_SENTENCE_WORD_COUNT:
        #sentence too long. pass
        continue
    if len([word for word in words_ if word.isupper()]) > 0:
        #its an acronym. pass
        continue
    if len([word for word in words_ if word[0].isupper()]) > 2:
        #more then 1 proper noun. pass
        continue
        
    sentence = re.sub(r'[^a-z ]', '', sentence.strip().lower())
    
    sentences.add(sentence)
    
    words_ = sentence.split(" ")
    for word in words_:
        #words.add(word)
        
        if word not in sentencesPerWord.keys():
            sentencesPerWord[word] = set()
            
        sentencesPerWord[word].add(sentence)

    #if len(sentences) >= MAX_SENTENCE_COUNT:
    #    break


for word in sentencesPerWord.keys():
    if len(sentencesPerWord[word]) >= MIN_WORD_PREVELANCE:
        words.add(word)

words = list(words)
words.sort()

print(len(sentences), "sentences and", len(words), "words out of", len(lines), "lines")

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



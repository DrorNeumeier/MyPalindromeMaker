import re
import random

dictionary_dir = "dictionaries/"

f = open(dictionary_dir + "/kjv.txt")

lines = f.readlines()

words = set()
sentences = set()
sentencesPerProperNouns = {}

MIN_WORD_PREVELANCE = 10

for line in lines:
    words_ = line.split(" ")[1:]
    
    sentence = " ".join(words_)
    sentence = re.sub(r'[^a-zA-Z ]', '', sentence.strip())
    
    while "  " in sentence:
        sentence = sentence.replace("  ", " ")
    
    sentence = sentence.strip()
    
    
    words_ = sentence.split(" ")
    for word_i in range(len(words_)):
        word = words_[word_i]
        if word_i>0 and word[0].isupper():
            #proper noun
            if word not in sentencesPerProperNouns.keys():
                sentencesPerProperNouns[word] = set()
    
            sentencesPerProperNouns[word].add(sentence)
        else:
            words.add(word.lower())

    sentences.add(sentence.lower())

print("is it in words?","mezahab" in words)
print("is it in proper nouns?", "mezahab" in sentencesPerProperNouns.keys())

wordsLeftOut = 0
for word in sentencesPerProperNouns.keys():
    if len(sentencesPerProperNouns[word]) >= MIN_WORD_PREVELANCE:
        words.add(word.lower())
    else:
        if word.lower() not in words:
            wordsLeftOut = wordsLeftOut + 1
            #print(word, sentencesPerProperNouns[word])

words = list(words)
words.sort()

print(len(sentences), "sentences and", len(words), "words with",wordsLeftOut, "proper nouns left out and",  len(lines), "lines")

sentences = list(sentences)
random.shuffle(sentences)

f = open(dictionary_dir + "kjv_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "kjv_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()

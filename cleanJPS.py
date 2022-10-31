import re
import csv
import random

dictionary_dir = "dictionaries/"
MIN_WORD_PREVELANCE = 10

words = set()
sentences = set()
sentencesPerProperNouns = {}

with open(dictionary_dir + 'jewish-publication-society-ot.csv', encoding='mac_roman') as csvfile:
     myReader = csv.reader(csvfile)
     for row in myReader:
        line = row[3]
        #print(row)
        
        if len(re.findall('[0-9]+', line)):
            print("has numbers. This should not happen")
            #has numbers. Just pick another one.
            continue
        
        sentence = re.sub(r'[^a-zA-Z ]', '', line.strip())
        
        while "  " in sentence:
            sentence = sentence.replace("  ", " ")
        
        sentence = sentence.strip()
        
        
        words_ = sentence.split(" ")
        for word_i in range(len(words_)):
            word = words_[word_i]
            #if word_i>0 and word[0].isupper():
            if word[0].isupper():
                #proper noun
                if word not in sentencesPerProperNouns.keys():
                    sentencesPerProperNouns[word] = set()
        
                sentencesPerProperNouns[word].add(sentence)
            else:
                words.add(word.lower())

        sentences.add(sentence.lower())

wordsLeftOut = 0
for word in sentencesPerProperNouns.keys():
    if len(sentencesPerProperNouns[word]) >= MIN_WORD_PREVELANCE:
        if word.lower() not in words:
            print(word, len(sentencesPerProperNouns[word]))
        words.add(word.lower())
        
    else:
        if word.lower() not in words:
            wordsLeftOut = wordsLeftOut + 1
            #print(word, "          ",len(sentencesPerProperNouns[word]))

words = list(words)
words.sort()

print(len(sentences), "sentences and", len(words), "words with",wordsLeftOut, "proper nouns left out")

sentences = list(sentences)
random.shuffle(sentences)

f = open(dictionary_dir + "jps_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "jps_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()

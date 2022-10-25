import re
import csv

dictionary_dir = "dictionaries/"
MIN_WORD_PREVELANCE = 1

sentences = set()
words = set()
sentencesPerWord = {}

with open(dictionary_dir + 'jewish-publication-society-ot.csv', encoding='mac_roman') as csvfile:
     myReader = csv.reader(csvfile)
     for row in myReader:
        line = row[3]
        #print(row)
        
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

     
        
for word in sentencesPerWord.keys():
    if len(sentencesPerWord[word]) >= MIN_WORD_PREVELANCE:
        words.add(word)
    else:
        print(word)

words = list(words)
words.sort()

print(len(sentences), "sentences and", len(words), "words")

f = open(dictionary_dir + "jps_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "jps_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()

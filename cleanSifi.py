import re

dictionary_dir = "dictionaries/"

f = open(dictionary_dir + "/internet_archive_scifi_v3.txt")

lines = f.readlines()

wordSet = {}
sentenceSet = set()

MIN_SENTENCE_WORD_COUNT = 3
MAX_SENTENCE_WORD_COUNT = 64
MIN_WORD_COUNT = 10

for line in lines:
    
    sentences = re.split('[.!:;?#]+', line)
    
    for sentence in sentences:
        sentence = re.sub(r'[^a-z ]', '', sentence.strip().lower())
        
        words = sentence.split(" ")
        for word in words:
            word = word.strip().lower()
            word = re.sub(r'\W+', '', word)
            
            if len(word) > 0:
                if word not in wordSet.keys():
                    wordSet[word] = 0
                wordSet[word] = wordSet[word] + 1
        
        if len(words) >= MIN_SENTENCE_WORD_COUNT and len(words) < MAX_SENTENCE_WORD_COUNT:
            sentenceSet.add(sentence)
        
print("before pruning")
print(len(wordSet))
print(len(sentenceSet))


wordSet_ = set()
for word in wordSet.keys():
    if wordSet[word] >= MIN_WORD_COUNT:
        wordSet_.add(word)
wordSet = wordSet_

sentenceSet_ = set()
for sentence in sentenceSet:
    words = set(sentence.split(" "))
    
    goodSentence = True
    for word in words:
        if word not in wordSet:
            goodSentence = False
            
    if goodSentence:
        sentenceSet_.add(sentence)
sentenceSet = sentenceSet_
    
print("after pruning")
print(len(wordSet))
print(len(sentenceSet))

wordSet = list(wordSet)
wordSet.sort()

f = open(dictionary_dir + "sci_words.txt", "w")
for word in wordSet:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "sci_sentences.txt", "w")
for sentense in sentenceSet:
    f.write("%s\n" %sentense)

f.close()



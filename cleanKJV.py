import re

dictionary_dir = "dictionaries"

f = open(dictionary_dir + "/kjv.txt")

lines = f.readlines()

kvj_wordSet = set()
kvj_sentenseSet = set()

MIN_SENTENCE_WORD_COUNT = 3
MAX_SENTENCE_WORD_COUNT = 64

for line in lines:
    words = line.split(" ")[1:]
    
    for word in words:
        word = word.strip().lower()
        word = re.sub(r'\W+', '', word)
        
        if len(word) > 0:
          kvj_wordSet.add(word)
    
    line = " ".join(words)
    sentences = re.split('[.!:;?]+', line)
    
    for sentense in sentences:
      sentense = re.sub(r'[^a-z ]', '', sentense.strip().lower())

      if sentense.count(" ") >= MIN_SENTENCE_WORD_COUNT-1 and sentense.count(" ") < MAX_SENTENCE_WORD_COUNT:
        kvj_sentenseSet.add(sentense)
        
f = open(dictionary_dir + "/kjv_words.txt", "w")
for word in kvj_wordSet:
    if len(word) > 0:
        f.write("%s\n" % word)
    
f.close()

f = open(dictionary_dir + "/kjv_sentences.txt", "w")
for sentense in kvj_sentenseSet:
    if len(sentense) > 0:
        f.write("%s\n" % sentense)
    
f.close()

print(len(kvj_wordSet))
print(len(kvj_sentenseSet))

print(list(kvj_wordSet)[:10])
print(list(kvj_sentenseSet)[:10])

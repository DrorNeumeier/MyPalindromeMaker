import re

dictionary_dir = "dictionaries/"

f = open(dictionary_dir + "/t8.shakespeare.txt")

text = f.read()

text = text.replace("\n\n", ".")

while "<<" in text:
    tag_in = text.index("<<")
    tag_out = text.index(">>", tag_in)
    
    #print(tag_in, tag_out)
    #print(text[tag_in:tag_out+2])
    
    text_ = text[0:tag_in]
    _text = text[tag_out+2:]
    text = text_+_text

text = text.replace("[", ".")
text = text.replace("]", ".")
text = text.replace("\n", " ")

while "  " in text:
    text = text.replace("  ", " ")
    
lines = text.split(".")

for line in lines:
    print(line)

wordSet = {}
sentenceSet = set()

MIN_SENTENCE_WORD_COUNT = 3
MAX_SENTENCE_WORD_COUNT = 64
MIN_WORD_COUNT = 1

for line in lines:
    
    sentences = re.split('[.!:;?]+', line)
    
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
    else:
        print(word)
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

f = open(dictionary_dir + "sks_words.txt", "w")
for word in wordSet:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "sks_sentences.txt", "w")
for sentense in sentenceSet:
    f.write("%s\n" %sentense)

f.close()




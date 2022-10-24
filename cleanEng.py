import pandas as pd
import re

dictionary_dir = "dictionaries/"

df = pd.read_csv(dictionary_dir + "in_domain_train.tsv", delimiter='\t', header=None, names=['sentence_source', 'label', 'label_notes', 'sentence'])

sentences = df.sentence.values
labels = df.label.values

sentences_ = []

for i in range(len(sentences)):
    if labels[i]:
        sentences_.append(sentences[i])
        
print(len(sentences), len(sentences_))

sentences = sentences_
sentences_ = []
words_ = set()

for sentence in sentences:
    sentence = re.sub(r'[^a-z ]', '', sentence.strip().lower())
    sentences_.append(sentence)
    
    words = sentence.split(" ")
    for word in words:
        words_.add(word.strip().lower())
        
words = words_
sentences = sentences_

print(len(words), len(sentences))

f = open(dictionary_dir + "eng_words.txt")
words = f.readlines()
words = set([word.strip().lower() for word in words])

for sentence in sentences:
    words_ = sentence.split(" ")

    for word in words_:
        if word not in words:
            print("adding word", word)
            words.add(word)
    
words = list(words)
words.sort()

f = open(dictionary_dir + "eng_words.txt", "w")
for word in words:
    f.write("%s\n" %word)

f.close()

f = open(dictionary_dir + "eng_sentences.txt", "w")
for sentense in sentences:
    f.write("%s\n" %sentense)

f.close()



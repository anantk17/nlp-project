from collections import Counter
import re
import math
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("english")

regex = r'([+-])\s([\s\S]*)\n'
positive_words = []
negative_words = []

for line in open("data_stop2.txt"):
    m = re.match(regex,line)
    sign = m.group(1)
    if sign == '+':
        line = m.group(2)
        positive_words += line.split()
    else:
        line = m.group(2)
        negative_words += line.split()

positive_words = [snowball_stemmer.stem(word) for word in positive_words]
negative_words = [snowball_stemmer.stem(word) for word in negative_words]

pos_corpus_length = len(positive_words)
neg_corpus_length = len(negative_words)

positive_count = Counter(positive_words)
negative_count = Counter(negative_words)

for key,value in positive_count.items():
    if not(len(key) > 1 and value >= 2):
        del positive_count[key]

for key,value in negative_count.items():
    if not(len(key) > 1 and value >= 2):
        del negative_count[key]

pos_vocab_length = len(positive_count)
neg_vocab_length = len(negative_count)

print positive_count.most_common(5)
print negative_count.most_common(5)

l = ['affordable','amazing','sadly']

l = [snowball_stemmer.stem(word) for word in l]

print l
for g_stem in l:
    print positive_count[g_stem],negative_count[g_stem]


for key,value in positive_count.items():
    positive_count[key] = (value + 1.0)/(pos_corpus_length + pos_vocab_length)

for key,value in negative_count.items():
    negative_count[key] = (value + 1.0)/(neg_corpus_length + neg_vocab_length)

for g_stem in l:
    print g_stem
    if positive_count[g_stem] > 0:
        print math.log(positive_count[g_stem],2)
    if negative_count[g_stem] > 0:
        print math.log(negative_count[g_stem],2)


def log_prob(s):
    words = s.split()
    words = [snowball_stemmer.stem(word) for word in words]
    pos_prob = 0
    neg_prob = 0
    for word in words:
        if positive_count[word] > 0:
            pos_prob += math.log(positive_count[word],2)
        else:
            prob = 1.0/(pos_corpus_length + pos_vocab_length)
            pos_prob += math.log(prob,2)
            
        if negative_count[word] > 0:
            neg_prob += math.log(negative_count[word],2)
        else:
            prob = 1.0/(neg_corpus_length + neg_vocab_length)
            neg_prob += math.log(prob,2)
    
    if pos_prob > neg_prob:
        print "+"
    else:
        print "-"

    return (pos_prob,neg_prob)
        





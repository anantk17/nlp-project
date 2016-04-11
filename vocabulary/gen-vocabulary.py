from collections import Counter
import re

def gen_words(line) :
    regex = r'([+-])\s([\s\S]*)\n'
    m = re.match(regex,line)
    line = m.group(2)
    return line.split()

def gen_words_and_bigrams(line) :
    words = gen_words(line)
    bigrams = zip(words, words[1:])
    bigrams = [ b for b in bigrams if len(b[0]) > 1 and len(b[1]) > 1 ] 
    bigrams = [ b[0] + "," + b[1] for b in bigrams ]
    return words , bigrams

def gen_vocab_unigram_file(data_file,vocab_file):
    """
    Generates unigram vocabulary file for the given data file
    """
    words = []
    for line in open(data_file):
        words= gen_words(line)
    c = Counter(words)
    #print c
    vocabulary = []
    #print c.items()
    with open(vocab_file,'w') as outfile:
        for key,value in c.items():
            #print key, value
            if len(key) > 1 and value >= 2 :
                vocabulary.append(key)
                outfile.write(key+"\n")

def gen_vocab_bigram_file(data_file,vocab_file):
    """
    Generates unigram and bigram vocabulary file for the given data file
    """

    vocab_unigram = []
    vocab_bigram = []
    for line in open(data_file):
        words ,  bigrams = gen_words_and_bigrams(line)
        vocab_unigram +=  words
        vocab_bigram += bigrams
    c = Counter(vocab_unigram)
    c1 = Counter(vocab_bigram)
    #print c
    vocabulary = []
    #print c.items()
    with open(vocab_file,'w') as outfile:
        for key,value in c.items():
            #print key, value
            if len(key) > 1 and value >= 2 :
                vocabulary.append(key)
                outfile.write(key+"\n")
        top_100 = [ w[0] for w in c1.most_common(100) ]
        for key,value in c1.items():
            #print key, value
            if key in top_100 :
                vocabulary.append(key)
                outfile.write(key+"\n")

gen_vocab_unigram_file('data-final-stop.txt','vocabulary.txt')
gen_vocab_bigram_file('data-final-stop.txt','vocabulary_2.txt')


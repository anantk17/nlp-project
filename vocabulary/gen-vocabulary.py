from collections import Counter
import re


def gen_vocab_file(data_file,vocab_file):
    """
    Generates vocabulary file for the given data file
    """

    regex = r'([+-])\s([\s\S]*)\n'
    words = []
    for line in open(data_file):
        m = re.match(regex,line)
        line = m.group(2)
        words += line.split()

    c = Counter(words)
    print c
    vocabulary = []
    print c.items()
    with open(vocab_file,'w') as outfile:
        for key,value in c.items():
            #print key, value
            if len(key) > 1 and value >= 2 :
                vocabulary.append(key)
                outfile.write(key+"\n")

gen_vocab_file('data-final-stop.txt','vocabulary.txt')

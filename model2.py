from collections import Counter
import re,math
from scipy.stats import norm

class NaiveBayesClassifier:
    
    def __init__(self):
        self.positive_unigram_count = Counter()
        self.negative_unigram_count = Counter()
        self.positive_bigram_count = Counter()
        self.negative_bigram_count = Counter()
        self.unigram_vocab_length = 0
        self.bigram_vocab_length = 0
        self.pos_unigram_corpus_length = 0
        self.neg_unigram_corpus_length = 0
        self.pos_bigram_corpus_length = 0
        self.neg_bigram_corpus_length = 0
        self.positive_lines = 0
        self.negative_lines = 0
        self.total_lines = 0

    def train_from_file(self,data_file):
        regex = r'([+-])\s([\s\S]*)\n'
        data = []
        labels = []
        for line in open(data_file):
            m = re.match(regex,line)
            data.append(m.group(2))
            labels.append(m.group(1))
        
        self.train(data,labels)

    def train(self,data,labels):
        self.total_lines = len(data)
        positive_unigrams = []
        negative_unigrams = []
        for sample in zip(labels,data):
            sign,line = sample
            if sign == '+':
                self.positive_lines += 1
                positive_unigrams += line.split()
            else:
                self.negative_lines += 1
                negative_unigrams += line.split()

        vocab_count = Counter(positive_unigrams + negative_unigrams)
        vocab_words = []

        self.positive_unigram_count = Counter(positive_unigrams)
        self.negative_unigram_count = Counter(negative_unigrams)

        for key,value in vocab_count.items():
            if not(len(key) > 1 and value >= 2):
                del vocab_count[key]
                #positive_unigrams = filter(lambda x: x != key, positive_unigrams)
                #negative_unigrams = filter(lambda x: x != key, negative_unigrams)
                del self.positive_unigram_count[key]
                del self.negative_unigram_count[key]

        self.unigram_vocab_length = len(vocab_count)

        self.pos_unigram_corpus_length = len(list(self.positive_unigram_count.elements()))
        self.neg_unigram_corpus_length = len(list(self.negative_unigram_count.elements()))

                
        #Training bigrams from here
        positive_bigrams = []
        negative_bigrams = []
        for sample in zip(labels,data):
            sign,line = sample
            if sign == '+':
                positive_bigrams += self.gen_bigrams(line)[1:]
            else:
                negative_bigrams += self.gen_bigrams(line)[1:]
        
        bigram_vocab_count = Counter(positive_bigrams + negative_bigrams)
        top_100 = [ w[0] for w in bigram_vocab_count.most_common(100) ]
        
        self.positive_bigram_count = Counter(positive_bigrams)
        self.negative_bigram_count = Counter(negative_bigrams)

        for key,value in bigram_vocab_count.items():
            if not key in top_100 :
                del vocab_count[key]
                #positive_bigrams = filter(lambda x: x != key, positive_bigrams)
                #negative_bigrams = filter(lambda x: x != key, negative_bigrams)
                del self.positive_bigram_count[key]
                del self.negative_bigram_count[key]
        
        self.bigram_vocab_length = len(bigram_vocab_count)
        
        self.pos_bigram_corpus_length = len(list(self.positive_bigram_count.elements()))
        self.neg_bigram_corpus_length = len(list(self.negative_bigram_count.elements()))

                
        
    def test(self,test_data):
        predicted_labels = []
        for line in test_data:
            predicted_labels.append(self.classify(line))

        return predicted_labels
   
    def pos_word_prob(self,w):
        return math.log((self.positive_unigram_count[w] + 1.0)/(self.pos_unigram_corpus_length + self.unigram_vocab_length),2)

    def neg_word_prob(self,w):
        return math.log((self.negative_unigram_count[w] + 1.0)/(self.neg_unigram_corpus_length + self.unigram_vocab_length),2)
        
    def pos_bigram_prob(self,w):
        #return math.log((self.positive_bigram_count[w] + 1.0)/(self.pos_bigram_corpus_length+self.bigram_vocab_length),2)
        return math.log((self.positive_bigram_count[w]*1.0)/(self.pos_bigram_corpus_length),2)

    def neg_bigram_prob(self,w):
        #return math.log((self.negative_bigram_count[w]+ 1.0)/(self.neg_bigram_corpus_length + self.bigram_vocab_length),2)
        return math.log((self.negative_bigram_count[w]*1.0)/(self.neg_bigram_corpus_length),2)

    def classify(self,line):
        pos_prob = 0.0
        neg_prob = 0.0
        
        bigrams = self.gen_bigrams(line,False)
        for bigram in bigrams:
                if self.negative_bigram_count[bigram] == 0 or self.positive_bigram_count[bigram] == 0 :
                    word = bigram.split(",")[1]
                    pos_prob += self.pos_word_prob(word)
                    neg_prob += self.neg_word_prob(word)
                else :
                    pos_prob += self.pos_bigram_prob(bigram)
                    neg_prob += self.neg_bigram_prob(bigram)
                    
        pos_prob = pos_prob + math.log((self.positive_lines*1.0 / self.total_lines),2)
        neg_prob = neg_prob + math.log((self.negative_lines*1.0 / self.total_lines),2)

        if pos_prob >= neg_prob:
            return "+"
        else:
            return "-"
    
    def gen_bigrams(self,line,train=True) :
        words = line.split()
        bigrams = zip(words, words[1:])
        if train :
            bigrams = [ b for b in bigrams if len(b[0]) > 1 and len(b[1]) > 1 ] 
        start = ["<s>,"+bigrams[0][0]]
        bigrams = [ b[0] + "," + b[1] for b in bigrams ]
        return start+bigrams
        
            
    def write_counts(self):
        #print self.positive_unigram_count
        #print self.negative_unigram_count
        print self.positive_bigram_count
        print self.negative_bigram_count
        #print self.unigram_vocab_length
        #print self.pos_unigram_corpus_length
        #print self.neg_unigram_corpus_length
        #print self.positive_lines
        #print self.negative_lines
        #print self.total_lines



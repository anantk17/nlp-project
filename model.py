from collections import Counter
import re,math

class NaiveBayesClassifier:
    
    def __init__(self):
        self.positive_count = Counter()
        self.negative_count = Counter()
        self.vocab_length = 0
        self.pos_corpus_length = 0
        self.neg_corpus_length = 0
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
        positive_words = []
        negative_words = []
        for sample in zip(labels,data):
            sign,line = sample
            if sign == '+':
                self.positive_lines += 1
                positive_words += line.split()
            else:
                self.negative_lines += 1
                negative_words += line.split()

        vocab_count = Counter(positive_words + negative_words)
        vocab_words = []
        for key,value in vocab_count.items():
            if not(len(key) > 1 and value >= 2):
                del vocab_count[key]
                positive_words = filter(lambda x: x != key, positive_words)
                negative_words = filter(lambda x: x != key, negative_words)

        self.vocab_length = len(vocab_count)

        self.pos_corpus_length = len(positive_words)
        self.neg_corpus_length = len(negative_words)

        self.positive_count = Counter(positive_words)
        self.negative_count = Counter(negative_words)

    def test(self,test_data):
        predicted_labels = []
        for line in test_data:
            predicted_labels.append(self.classify(line))

        return predicted_labels
   
    def pos_word_prob(self,w):
        return math.log((self.positive_count[w] + 1.0)/(self.pos_corpus_length + self.vocab_length),2)

    def neg_word_prob(self,w):
        return math.log((self.negative_count[w] + 1.0)/(self.neg_corpus_length + self.vocab_length),2)
    
    def classify(self,line):
        pos_prob = 0.0
        neg_prob = 0.0
        
        words = line.split()
        for word in words:
                pos_prob += self.pos_word_prob(word)
                neg_prob += self.neg_word_prob(word)
        
        pos_prob = pos_prob + math.log((self.positive_lines*1.0 / self.total_lines),2)
        neg_prob = neg_prob + math.log((self.negative_lines*1.0 / self.total_lines),2)

        if pos_prob >= neg_prob:
            return "+"
        else:
            return "-"

    def write_counts(self):
        print self.positive_count
        print self.negative_count
        print self.vocab_length
        print self.pos_corpus_length
        print self.neg_corpus_length
        print self.positive_lines
        print self.negative_lines
        print self.total_lines



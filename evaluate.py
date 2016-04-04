import re,math
import numpy as np
from model import NaiveBayesClassifier
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score,f1_score,recall_score

def evaluate(data_file):
    regex = r'([+-])\s([\s\S]*)\n'
    data = []
    labels = []
    for line in open(data_file):
        m = re.match(regex,line)
        data.append(m.group(2))
        labels.append(m.group(1))

    X = np.array(data)
    y = np.array(labels)

    kf = KFold(1000,n_folds=10)

    train_data = []
    test_data = []
    test_labels = []

    k = 0

    acc = []
    f_score = []
    recall =[]

    for train_index, test_index in kf:
        train_data,train_labels = X[train_index], y[train_index]
        test_data, test_labels = X[test_index],y[test_index]
        
        model = NaiveBayesClassifier()
        model.train(train_data,train_labels)

        result = model.test(test_data)
        #print result,len(result)
        a,f,r =  accuracy_score(test_labels,result),f1_score(test_labels,result,pos_label='+'),recall_score(test_labels,result,pos_label='+')
        acc.append(a)
        f_score.append(f)
        recall.append(r)

    print "accuracy=",np.mean(acc)
    print "f_score=",np.mean(f_score)
    print "recall=",np.mean(recall)

evaluate('data-final-stop.txt')

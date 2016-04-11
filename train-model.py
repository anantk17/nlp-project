from model2 import NaiveBayesClassifier
import pickle

model = NaiveBayesClassifier()
model.train_from_file('data-final-stop.txt')

model.write_counts()

pickle.dump(model, open('model2.p','wb'))


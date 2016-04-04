from model import NaiveBayesClassifier
import pickle

model = NaiveBayesClassifier()
model.train_from_file('data-final-stop.txt')

model.write_counts()

pickle.dump(model, open('model.p','wb'))


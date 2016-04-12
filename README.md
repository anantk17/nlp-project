# nlp-project
Repository for the Natural Language Processing Course Project
## Team Members
- Anant Kandikuppa B120519CS
- Hemant Pugaliya B120787CS
- Pranay Dhariwal B120762CS

# Dependencies
- Python(version 2.7)
- Numpy ```pip install -U numpy```
- scikit-learn ```pip install -U scikit-learn```

# Contents
- data-collection/ : Contains our chosen dataset
- stop-word-removal/ : Contains cleaned dataset without stopwords and the requisite python code for achieving the same
- vocabulary/ : Contains the vocabulary file and the code required to obtain it
- evaluate.py : Code for performing 10 fold cross validation
- model.p : Pickled model obtained by training our model on the entire dataset
- model.py : Contains the definition for the NaiveBayesClassifier Class used to represent our model
- train-model.py : Code to train and pickle a model

# Unigram Model and Bigram Model
The NaiveBayesClassifier Class defined in model.py and model2.py is used to represent a unigram model and a bigram model respectively.

It provides the following methods:
- ```__init__(self)``` : Default constructor
- ```train_from_file(self,data_file)```: Trains a model instance using the data read from  ```data_file```
- ```train(self,data,labels)```: Trains a model using list of sentences as ```data``` and their corresponding labels as ```label```
- ```test(self,test_data)``` : Returns a set of predicted labels corresponding to the list of sentences passed as ```test_data```
- ```pos_word_prob(self,word)```: Returns the conditional probability of a word being in the positive class
- ```neg_word_prob(self,word)``` : Returns the conditional probability of a word being in the negative class
- ```classify(self,line)``` : Returns the predicted class of a sentence passed as ```line```
- ```write_counts(self,line)``` : Prints the counts of attributes for debugging purposes

# Results 
For Part A,we obtained an accuracy of __91.9%__ after 10 fold cross validation of the model on our training data.
For Part B,we obtained an accuracy of __92.0%__ after 10 fold cross validation of the model on our training data.

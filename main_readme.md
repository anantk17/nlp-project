# nlp-project
Repository for the Natural Language Processing Course Project
## Team Members
- Anant Kandikuppa B120519CS
- Hemant Pugaliya B120
- Pranay Dhariwal

# Contents
- data-collection/ : Contains our chosen dataset
- stop-word-removal/ : Contains cleaned dataset without stopwords and the requisite python code for achieving the same
- vocabulary/ : Contains the vocabulary file and the code required to obtain it
- evaluate.py : Code for performing 10 fold cross validation
- model.p : Pickled model obtained by training our model on the entire dataset
- model.py : Contains the definition for the NaiveBayesClassifier Class used to represent our model
- train-model.py : Code to train and pickle a model

# Unigram Model
The NaiveBayesClassifier Class is used to represent the model.

It has the following attributes:
- ```positive_count``` : A dictionary storing the counts of each word in the positive class
- ```negative_count``` : A dictionary storing the counts of each word in the positive class
- ```vocab_length``` : The length of vocabulary obtained from the entire corpus
- ```pos_corpus_length``` : The count of words belonging to the positive class in the corpus
- ```neg_corpus_length``` : The count of words belonging to the negative class in the corpus
- ```positive_lines``` : The number of sentences that belong to the positive class in the dataset
- ```negative_lines``` : The number of sentences that belong to the negative class in the dataset

And provides the following methods:
- ```__init__(self)``` : Default constructor
- ```train_from_file(self,data_file)```: Trains a model instance using the data read from  ```data_file```
- ```train(self,data,labels)```: Trains a model using list of sentences as ```data``` and their corresponding labels as ```label```
- ```test(self,test_data)``` : Returns a set of predicted labels corresponding to the list of sentences passed as ```test_data```
- ```pos_word_prob(self,word)```: Returns the conditional probability of a word being in the positive class
- ```neg_word_prob(self,word)``` : Returns the conditional probability of a word being in the negative class
- ```classify(self,line)``` : Returns the predicted class of a sentence passed as ```line```
- ```write_counts(self,line)``` : Prints the counts of attributes for debugging purposes

# Results 
We obtained an accuracy of __88.8%__ after 10 fold cross validation of the model on our training data.
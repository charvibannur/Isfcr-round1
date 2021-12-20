# Spam Detection Model
# Dataset:

Data is the essential ingredients before we can develop any meaningful algorithm. Knowing where to get your data can be a very handy tool.I've attached the Dataset I have used. This dataset classifies the data into two categories- Ham and Spam. Ham looks like a normal email reply to another person, which is not difficult to classified as a ham. The spam data looks similar to one of those junk advertising emails.

# Test-Train split:

It is important to split your data set to training set and test set, so that you can evaluate the performance of your model using the test set before deploying it in a production environment.
One important thing to note when doing the train test split is to make sure the distribution of the data between the training set and testing set are similar.
What it means in this context is that the percentage of spam email in the training set and test set should be similar.

# Data preprocessing:

Text Cleaning is a very important step in machine learning because your data may contains a lot of noise and unwanted character such as punctuation, white space, numbers, hyperlink and etc.
Some standard procedures that people generally use are:
1.convert all letters to lower/upper case
2.removing numbers  
3.removing punctuation  
4.removing white spaces  
5.removing hyperlink  
6.removing stop words such as a, about, above, down, doing and the list goes on…  
7.Word Stemming  
8.Word lemmatization  

# Count Vectorizer:

First we need to input all the training data into CountVectorizer and the CountVectorizer will keep a dictionary of every word and its respective id and this id will relate to the word count of this word inside this whole training set.

# Naive Bayes Classifier:

Gaussian Naive Bayes is a variant of Naive Bayes that follows Gaussian normal distribution and supports continuous data.

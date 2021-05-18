import csv
from nltk import word_tokenize
from joblib import load
with open('vocab.txt') as vocab:
    vocab_string = vocab.readline()
    vocab_list = vocab_string.split(",")
    model = load('model.joblib')
    while True:
        comment = input("enter your comment : ")
        words = word_tokenize(comment)
        comment_vector = []
        for word in vocab_list:
            if word in words:
                comment_vector.append(1)
            else:
                comment_vector.append(0)
        print(comment_vector)
        prediction = model.predict([comment_vector])
        print(prediction)

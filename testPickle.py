import pickle
import csv
from nltk import word_tokenize
from joblib import load
from sklearn.metrics import accuracy_score
from textblob import TextBlob


filename = 'finished_model.sav'
model = pickle.load(open(filename, 'rb'))
with open('vocab.txt') as vocab:
    vocab_string = vocab.readline()
    vocab_list = vocab_string.split(",")
    csv_data = []
    csv_actual = []
    with open('test_csv.csv', 'r') as vector_data:
        reader = csv.DictReader(vector_data)
        for row in reader:
            corrected_text = TextBlob(row['text'])
            print(corrected_text)
            print(type(str(corrected_text)))
            words = word_tokenize(str(corrected_text))
            print(words)
            sentence = [word.lower() for word in words if word.isalpha()]
            print(sentence)
            comment_vector = []
            for word in vocab_list:
                if word in sentence:
                    comment_vector.append(1)
                else:
                    comment_vector.append(0)
            print(comment_vector)
            csv_data.append(comment_vector)
            print(row['positivity'])
            csv_actual.append(int(row['positivity']))

        prediction = model.predict(csv_data)
        print(prediction)
        print(csv_actual)
        print("accuracy score : ", accuracy_score(csv_actual, prediction))
        print(prediction)

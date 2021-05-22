import pandas as pd
import csv
import pickle
import ast
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import accuracy_score
from joblib import dump, load

train_data = []
with open('vector_data.csv', 'r') as vector_data:
    reader = csv.DictReader(vector_data)
    for row in reader:
        print(row['text'] + '\n')
        stringlist = row['vector'].split(",")
        intlist = list(map(int, stringlist))
        print(type(intlist))
        print(intlist)
        train_data.append(intlist)
print(train_data)
vector_data = pd.read_csv('vector_data.csv')
print(vector_data.head())
X = train_data
# print(X)
y = vector_data['positivity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)
print("accuracy score : ", accuracy_score(y_test, y_pred))

# total = 0
# correct = 0
# for i in range(len(X_test)):
#     total = total + 1
#     if svclassifier.predict([X_test[i]]) == [y_test[i]]:
#         correct = correct + 1
# accuracy = (correct / total) * 100
# print('accuracy score is : ' + accuracy)
# dump(svclassifier, 'model.joblib')
# print("model saved")
filename = 'finished_model.sav'
pickle.dump(svclassifier, open(filename, 'wb'))


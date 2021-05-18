from nltk import word_tokenize
import csv

vocab = []
sentence = []
line_no = 0
with open('new_data.csv') as readFile:
    reader = csv.reader(readFile)
    next(reader)
    for row in reader:
        line_no = line_no+1
        #print(row)
        words = word_tokenize(row[1])
        sentence = [word.lower() for word in words if word.isalpha()]
        #print(sentence)
        for word in sentence:
            if word not in vocab:
                vocab.append(word)
        print(line_no)
with open('vocab.txt','w') as textFile:
    string = ",".join(vocab)
    textFile.write(string)
import csv
from nltk import word_tokenize

with open('vocab.txt') as vocabfile:
    vocab_str = vocabfile.readline()
    list1 = vocab_str.split(",")
    with open('new_data.csv') as file:
        with open('vector_data.csv', 'w', newline='') as writeFile:
            fieldnames = ['rating', 'text', 'positivity', 'vector']
            reader = csv.reader(file)
            writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
            writer.writeheader()
            next(reader)
            for row in reader:
                print(row[1])
                words = word_tokenize(row[1])
                sentence = [word.lower() for word in words if word.isalpha()]
                print(sentence)
                vector = []
                for word in list1:
                    if word in sentence:
                        vector.append(str(1))
                    else:
                        vector.append(str(0))
                vector = ",".join(vector)
                writer.writerow({'rating': row[0], 'text': row[1], 'positivity': row[2], 'vector': vector})


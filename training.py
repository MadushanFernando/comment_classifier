import numpy as np
import pandas as pd
import csv

with open('vector_data.csv', 'r') as vector_data:
    reader = csv.DictReader(vector_data)
    for row in reader:
        print(row['text']+'\n')
        stringlist = row['vector'].split(",")
        intlist  = list(map(int,stringlist))
        print(type(intlist))
        print(intlist)
        break

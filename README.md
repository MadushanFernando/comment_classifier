# Sentiment Analysis using bag of words

### Introduction

NLP is analyzing, understanding, and generating the languages that humans use naturally to interface with 
computers in both written and spoken contexts using natural human languages instead of computer 
languages. There are few steps in Natural Language Processing.
  - Morphological and Lexical Analysis (analyzing the structure of words and dividing the text into 
    paragraphs, words, and sentences)
  - Syntactic Analysis (analyzing sentences to interpret the grammatical structure)
  - Semantic Analysis (Theses structures are given meaning from dictionary or exact meaning from 
    context)
  - Discourse Integration (the meaning of a sentence is dependent upon sentences that precede it. Such 
    as, “Tom had an apple. Adam wants it.”. To understand what “it” is we need to read the sentence 
    that precedes it.)
  - Pragmatic Analysis (what is intended by the natural language text and how should it be interpreted?
  
does the speaker mean what they literally say, or do they imply another meaning? such as sarcasm)
Text is a technique that computers use to extract worthwhile information from the human language in a 
smart and efficient manner. Researchers and developers can use this method to assemble diverse and 
unorganized data in a structured form. In this process, documents are disintegrated for hassle-free 
management of data pieces, simply put unstructured text gets converted into structured data.
The bag-of-words (BOW) model is a representation that turns arbitrary text into fixed-length vectors by 
counting whether a certain word appear or not. This process is often referred to as vectorization. A bag-of-words is a representation of text that describes the occurrence of words within a document. It involves two 
things: a vocabulary of known words, a measure of the presence of known words. It is called a “bag” of 
words because any information about the order or structure of words in the document is discarded. The 
model is only concerned with whether known words occur in the document, not where in the document.
Despite being a relatively basic model, BOW is often used for Natural Language Processing (NLP) tasks 
like Text Classification. 


### Training the model
To make it easier for debugging and to save time we devided the complete code into seperate files

  #### 1. Creating_bow.py
    This file creates the bag of words in 'vocab.txt' file using comments in 'new_data.csv' as input.
  #### 2. Vocab.py
    Converts comments in 'new_data.csv' file into vectors and saves them in 'vector_data.csv' file.
  #### 3. new_training.py
    Creates the svm model using vectors in 'vector_data.csv' file as training data and saves the model in 'model.joblib' file and in 'finished_model.sav' file for later use.
    
    [You can see the final model in action in this link](https://colab.research.google.com/drive/1gdTvkF6Za92XPZHbgyMpiTcg8nJe4MdQ?usp=sharing) 
  


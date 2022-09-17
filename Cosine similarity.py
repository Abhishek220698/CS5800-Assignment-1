# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Defining the documents
doc1 = "Soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "I support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"


# Use the following words as terms to create your document matrix
# [soccer, my, favorite, sport, I, like, one, support, olympic, game]
# --> Add your Python code here
def document_matrix(doc):
   train_set = 'soccer my favorite sport I like one support olympic games'
   list = [doc, train_set]   
   vectorizer = TfidfVectorizer(stop_words="english")
   vectorizer.fit_transform(list)
   document_matrix = vectorizer.vocabulary_
   print(document_matrix)



# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
# --> Add your Python code here

def compute_similarity(x, y):
    list_text = [x, y]
    
    # converts text into vectors with the TF-IDF 
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit_transform(list_text)
    tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])
    
    # computes the cosine similarity
    cs_score = cosine_similarity(tfidf_text1, tfidf_text2)
    
    return np.round(cs_score[0][0],2)

def get_highest_cosine(*args):
    list = [*args]
    if(len(list) == 2):
        score = compute_similarity(list[0], list[1])
        print(f"The cosine similarity for the documents is {score}")
    else:
        x = list[0]; y = list[1]
        for i in range(0, len(list)):
            for j in range(i+1, len(list)):
                score = compute_similarity(list[i],list[j])
                if (score  > compute_similarity(x, y)):
                    x = list[i]; y = list[j]
        indexofx = list.index(x)
        indexofy = list.index(y)
    
        score = compute_similarity(x,y)
    
        print(f"The most similar documents are doc {indexofx} and doc {indexofy}, their cosine similarity is {score}")


# Print the highest cosine similarity following the template below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here

""" 
    Prints the position of the documents from the arguments passed 
    Array counting from zero
    Alternatively the template string could be changed
"""
get_highest_cosine(doc2, doc3, doc4)











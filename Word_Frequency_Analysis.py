""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string #Used to manipulate strings and remove punctuation
import itertools #Used to combine elements of nested lists into a single list
from collections import Counter #Used to count the frequency of words in the text

def replace_all(text, dic): #Looks at text and replaces all occurances of each key in dic with the given value
    for key, value in dic.iteritems(): #Iterates through all the keys and values of dic
        text = text.replace(key, value) #replaces key with value in text
    return text

def get_word_list(file_name): #Sorts a text file into a list of individual words
    f = open(file_name,'r') #Opens the file
    lines = f.readlines() #Reads each line of the text file
    punctuation = string.punctuation #Creates a string of every kind of punctuation in the English language
    bad_text = {'\r': '', '\n': '', '\xe2': '', '\x80': '', '\x94': '', '\x99': '', '\x98': '', '\xc3': '', '\xb6': '', '\xa6': '', '\x93': '' } #Assigns new lines and unknown characters to empty strings
    curr_line = 0
    text = []
    words = []
    lower_words = []
    while lines[curr_line].find('FROM PRE-HISTORIC TO MODERN TIMES.') == -1: #Identifies the first line before the start of the text and removes it and everythong before it
        curr_line += 1
    lines = lines[curr_line+1:]

    for line in lines:
        line = replace_all(line, bad_text) #Removes all formatting as indicated in bad_text
        for punct in punctuation:
            line = line.replace(punct,'') #Removes all punctuation in the text
        if len(line) != 0: #If a line of the text is empty it is not included in the new list
            text.append(line)
    for line in text:
        words.append(re.sub("[^\w]", " ",  line).split()) #Separates every line into a list of all the words contained in it
    all_words = list(itertools.chain.from_iterable(words)) #Combines the nested lists of words into a single list containing every word
    for word in all_words:
        lower_words.append(word.lower()) #Makes a new list containing all the words in the text in lowercase characters
    return lower_words

def get_top_n_words(word_list, n): #Prints the n most common words in the text
    print Counter(word_list).most_common(n) #Uses the Counter function in collections and prints the n most common words using the .most_common() function


get_top_n_words(get_word_list('Bread.txt'), 16)

""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

##TODO: debug---
	#-why ' ' most common thing
	#-all lowercase
	#-what's up with the location thing

import string
from pattern.web import *

def get_word_list(full_text):
	cut=full_text.split('End of the Project Gutenberg EBook of Oliver Twist, by Charles Dickens')[0] #manual stripping of the header and footer
	cut2= cut.split('Produced by Peggy Gaugy and Leigh Little.  HTML version by Al Haines.')[1]
	wordlist=cut2.split(' ') #splits the book by words and gives a list of words
	for word in wordlist:
		word=word.lower().strip() #makes every word lowercase 
		word =word.translate(None, string.punctuation) #strips all punctuation
	while ('\n' in wordlist):
		wordlist.remove('\n')
	return wordlist
	

def get_top_n_words(word_list, n):
	#create a list of lists
	numList=[] #creates empty lists
	wordList=[]
	for i in range (0,n):
		wordList.append('filler') #populates lists as much as n with fillers
		numList.append(0)

	for word in word_list:
		frequency=count_how_many(word_list,word)
		location=0
		for i in numList:
			if(frequency>i):
				location=location+1 #determining if the word belongs in the list/where it belongs
		if(location>0):
			numList.insert(location,frequency) #inserts the new updated values in the right places
			wordList.insert(location,word)
			numList.pop(0)
			wordList.pop(0)

	for word in wordList:
		print word


def count_how_many(word_list, word):
	count=0
	for newWord in word_list:
		if (newWord==word):
			count=count+1 #counts how many of a word exist in a list of words
			word_list.remove(newWord) #if it exists, remove it to avoid double counting
	return count

	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""

full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download() #downloading the text

new_word_list=get_word_list(full_text)
get_top_n_words(new_word_list, 5)
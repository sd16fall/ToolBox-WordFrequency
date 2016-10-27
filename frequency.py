""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

# Toolbox 2 : Anderson Ang Wei Jian
# Word Frequency Analysis Toolkit


import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# Opens file for reading
	f = open(file_name,'r')
	# Saves the lines of the file into a list in lowercase form
	lines = f.readlines()
	# Closes the file
	file.close
	# Initalizes a variable to traverse the list
	curr_line = 0
	# Locates the sentence stated below by iterating through the lines
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	# Based on last point, splices away the content before the line & saves it
	lines = lines[curr_line+1:]

	# creates a list to append individual words to
	words_list = []

	# Breaks the lines up into individual words of uniform hierachy in a single-level list
	# Also removes any whitespace trailing or leading each word
	for i in range(len(lines)):
		# Appends the words in a list in lower case
		words_list.extend(lines[i].lower().split())

	# Iterates through each word in the list & removes the punctuation at the EDGES
	# Note: Space complexity is observed here - 0(2) employs reuse of lists, saving memory
	words_list = [word.strip(string.punctuation) for word in words_list]

	# Returns the processed list
	return words_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	# create an empty dictionary
	word_counts = {}

	# traverses the word_list to find similarities and increment count
	for word in word_list:
		word_counts[word] = word_counts.get(word, 0) + 1

	# sorts and enrolls the dictionary terms into a list
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)

	# returns n most frequent terms
	return ordered_by_frequency[:n]

if __name__ == '__main__':
	# passes filename to get_word_list function
	word_list = get_word_list("dontmarry.txt")
	print get_top_n_words(word_list, 100)

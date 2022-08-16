"""
File: boggle.py
Name: Max Huang
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()

	dict_ = read_dictionary()
	board = []
	for i in range(1, 5):
		letters = input(f'{i} row of letters: ').lower()
		if len(letters) > 7 or letters[1] != ' ' or letters[3] != ' ' or letters[5] != ' ':
			print('Illegal input')
			break
		else:
			board.append(letters.split())
	print(board)
	find_words(board, dict_)

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(board, dict_):
	word_lst = []
	for i in range(4):
		for j in range(4):
			position = []
			first_ch = board[i][j]
			position.append([i, j])
			find_words_helper(board, first_ch, word_lst, i, j, position, dict_)
	print(f'There are {len(word_lst)} words in total.')


def find_words_helper(board, word, word_lst, x, y, position, dict_):
	# Base Case!
	if len(word) >= 4 and word in dict_ and word not in word_lst:
		print('Found: ', word)
		word_lst.append(word)

	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= x + i <= 3 and 0 <= y + j <= 3 and [x + i, y + j] not in position:
				word += board[x + i][y + j]
				position.append([x + i, y + j])

				if has_prefix(word, dict_):
					find_words_helper(board, word, word_lst, x + i, y + j, position, dict_)

				word = word[:-1]
				position.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		english_dictionary = []
		for line in f:
			english_dictionary.append(line.strip())
		return english_dictionary


def has_prefix(sub_s, dict_):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_: List, english dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

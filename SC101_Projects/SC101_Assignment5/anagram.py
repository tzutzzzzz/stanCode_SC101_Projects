"""
File: anagram.py
Name: Max Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
    word = input('Find anagrams for: ')
    while True:
        if word == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(word)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            word = input('Find anagrams for: ')


def read_dictionary():
    with open(FILE, 'r') as f:
        english_dictionary = []
        for line in f:
            english_dictionary.append(line.strip())
        return english_dictionary


def find_anagrams(s):
    """
    :param s: Enter a random english word.
    :return: Give you all the anagrams of the word entered.
    """
    anagrams = []
    count = [0]
    counter = [0]
    find_anagrams_helper(s, '', [], anagrams, count, counter)
    print(f'{count[0]} anagrams: {anagrams}')
    print(counter)


def find_anagrams_helper(word, current_s, index_lst, anagrams, count, counter):
    counter[0] += 1
    if len(current_s) == len(word):
        if current_s in read_dictionary():
            if current_s not in anagrams:
                count[0] += 1
                print('Searching...')
                print(f'Found: {current_s}')
                anagrams.append(current_s)
    # Words may have repeat alphabet, use index of alphabet to avoid it
    for i in range(len(word)):
        if i not in index_lst:
            current_s += word[i]
            index_lst.append(i)
            if has_prefix(current_s):
                find_anagrams_helper(word, current_s, index_lst, anagrams, count, counter)
            current_s = current_s[: len(current_s) - 1]
            index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: Random english string wanted to check.
    :return: Boolean result according to whether dictionary has word start with entered string.
    """
    for word in read_dictionary():
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

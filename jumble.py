#!/usr/bin/env python3

import argparse
import itertools


def jumble(jumble_dict, word):
    """Jumble solver

    Args:
        jumble_dict (dict[list[str]]): Dictionary contained hashed words
        word (str): Input word
    Returns
        list of str: Jumble solutions
    """
    words = {}
    for i in range(2, len(word)+1):  # Getting combinations of words from 2 to word length
        for combination in itertools.combinations(word.lower(), i):
            combination = "".join(sorted(combination)) # sorting word so we can find it on dict
            if combination in jumble_dict:
                # Adding list to dict as keys
                words.update(dict.fromkeys(jumble_dict[combination]))
    if word in words: 
        del words[word] # Removing input word from result
    return words.keys()  # Getting dict keys as a list


def parse_word_list_file(file_name):
    """Creates a jumble dictionary from a file containing a list of words

    Args:
        file_name (str): Name of file containing a list of words

    Returns:
        dict[list[str]]: Jumble dictionary, keys are sorted words, values are list of original words
    """
    jumble_dict = {}

    with open(file_name, "r") as word_list:
        for word in word_list:
            word = word.strip()  # Removing trailing and whitespace characters
            # Sorting the word, so we can easily find anagrams
            key = "".join(sorted(word.lower()))
            # setdefault searches for a key and returns its value if found. If not found, creates a list on that key
            jumble_dict.setdefault(key, []).append(word)
    return jumble_dict


if __name__ == "__main__":
    # Creates nice argument parser with help
    parser = argparse.ArgumentParser(description='Jumble solver.')
    parser.add_argument('word_list', type=str, help='Word list file')
    parser.add_argument('word', type=str, help='Jumble word')
    args = parser.parse_args()

    jumble_dict = parse_word_list_file(args.word_list)
    jumble_words = jumble(jumble_dict, args.word)

    for word in jumble_words:
        print(word)

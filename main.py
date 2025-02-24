from stats import get_num_words
import sys

def main():
    if len(sys.argv) != 2:
	    print("Usage: python3 main.py <path_to_book>")
	    sys.exit(1)

    with open(sys.argv[1]) as f:
        file_contents = f.read()
    dictionary = char_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_num_words(file_contents)
    print(f"{num_words} words found in the document \n")
    for char in dictionary:

        if char.isalpha() is True:
            print(f"{char}: {dictionary[char]}")
    print("--- End report ---")

def char_count(file):
    dictionary = {}
    for char in file:
        char_lower = char.lower()
        if char_lower not in dictionary:
            dictionary[char_lower] = 1
        else:
            dictionary[char_lower] += 1
    return dictionary

main()

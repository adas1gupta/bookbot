from stats import get_num_words

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    dictionary = char_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_num_words(file_contents)
    print(f"{num_words} words found in the document \n")
    for char in dictionary:

        if char.isalpha() is True:
            print(f"The \'{char}\' character was found {dictionary[char]} times")
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

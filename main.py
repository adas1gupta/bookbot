
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(char_count(file_contents))

def word_count(file):
    return len(file.split())

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
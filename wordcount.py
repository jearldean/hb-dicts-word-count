import sys

def word_counts(path):
    """Count words in file.
    parameter: a path with strings
    prints word and its word count"""

    text_to_count = open(path)
    punctuation_marks = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    word_counts = {}

    for line in text_to_count:
        line = line.rstrip().split(" ")

        for word in line:
            for mark in punctuation_marks:
                word = word.replace(mark, "")
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    for key, item in word_counts.items():
        print(key, item)
    print(f"\nThat was {len(word_counts)} different words.")


# path = "test.txt"
# word_counts(path)

# path = "twain.txt"
path = sys.argv[1]
word_counts(path)

def word_counts(path):
    """Count words in file.
    parameter: a path with strings
    prints word and its word count"""

    text_to_count = open(path)

    word_counts = {}

    for line in text_to_count:
        line = line.rstrip().split(" ")

        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1

    for key, item in word_counts.items():
        print(key, item)


path = "test.txt"
word_counts(path)
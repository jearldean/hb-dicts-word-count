import sys
import re
from collections import Counter


def word_counts(path):
    """Count words in file.
    parameter: a path with strings
    prints word and its word count"""

    words = re.findall(r'\w+', open(path).read().lower())
    words_dict_items = Counter(words).items()
    for each_tuple in words_dict_items:
        print(f"{each_tuple[0]}\t{each_tuple[1]}")

    print(f"\nThat was {len(words_dict_items)} different words.")


path = sys.argv[1]
word_counts(path)

import sys
import re
from collections import Counter


def word_counts(path, sort_type='1'):
    """Count words in file.
    parameter: a path with strings
    prints word and its word count"""

    words = re.findall(r'\w+', open(path).read().lower())
    words_dict_items = Counter(words).items()

    if sort_type == '1':  # sort by keys
        for key, value in sorted(words_dict_items):
            print(f"{key}\t{value}")
    elif sort_type == '2':  # sort by values ascending
        sort_dict = dict(sorted(words_dict_items, key=lambda x:x[1]))
        for key, value in sort_dict.items():
            print(f"{key}\t{value}")
    else:   # sort by values descending
        sort_dict = dict(sorted(words_dict_items, key=lambda x:-x[1]))
        for key, value in sort_dict.items():
            print(f"{key}\t{value}")

    print(f"\nThat was {len(words_dict_items)} different words.")


path = sys.argv[1]
sort_type = sys.argv[2]
word_counts(path, sort_type)

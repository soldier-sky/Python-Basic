"""Example to understand how package aka libraries are created in Python"""

from collections import Counter

def count_in_list(in_list, word):
    count = Counter(in_list)
    return count[word]
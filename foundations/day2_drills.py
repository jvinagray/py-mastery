#1.
def unique(seq):
    seen = {}
    for index, item in enumerate(seq):
        if item not in seen:
            seen[item] = index
    return(list(seen))

seq = [1, 2, 8, 4, 2, 5, 8, 1, 6, 8, 5, 3, 4, 7, 8, 5]
print(unique(seq))

#2.
def flatten(nested_list):
    flattened = [item for sublist in nested_list for item in sublist]
    return flattened

nested_list = [[1], [2, 3, 4], [5, 6, 7], [8]]

print(flatten(nested_list))

#3.
def group_by_key(tuple_list):
    seen = {}
    for t in tuple_list:
        k, v = t
        if k not in seen:
            seen[k] = [v]
        else:
            seen[k].append(v)
    return seen 

print(group_by_key([("a",1),("b",2),("a",3)]))
#4.
def frequency_count(string):
    seen = {}
    words = string.split()
    for word in words:
        if word not in seen:
            seen[word] = 1
        else:
            seen[word] += 1
    return seen

print(frequency_count("hi i am bob bob is a nickname i like the name hi bob"))

#5.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
seen = {x:x**2 for x in nums}
print(seen)

import re

def ordered_frequency_count(string):
    seen = {}
    words = re.split(r'[,.\s]', string)
    for word in words:
        if word not in seen:
            seen[word] = 1
        else:
            seen[word] += 1
    sorted_items_t = sorted(seen.items(), key=lambda item: item[1], reverse=True)
    sorted_seen = dict(sorted_items_t)
    return sorted_seen

print(ordered_frequency_count("hi i am bob bob is a nickname i like the name hi bob"))

def top_num_frequency(string, num):
    seen = {}
    words = re.split(r'[,.\s]', string)
    for word in words:
        if word not in seen:
            seen[word] = 1
        else:
            seen[word] += 1
    sorted_tuples = sorted(seen.items(), key=lambda item: item[1], reverse=True)
    top_num_dict = {k: v for i, (k, v) in enumerate(sorted_tuples) if i < num}
    return top_num_dict

print(top_num_frequency("hi i am bob bob is a nickname i like the name hi bob", 2))

def anagram_grouper(words):
    anagrams = {}
    for word in words:
        sorted_chars = ''.join(sorted(list(word)))
        if sorted_chars not in anagrams:
            anagrams[sorted_chars] = [word]
        else:
            anagrams[sorted_chars].append(word)
    return anagrams

words = ["eat","tea","tan","ate","nat","bat"]
print(anagram_grouper(words))
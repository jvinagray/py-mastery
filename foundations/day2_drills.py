#1.
def unique(seq):
    seen = {}
    for index, item in enumerate(seq):
        if item not in dict:
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
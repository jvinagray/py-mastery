with (open('output.txt','w', encoding='utf-8'))as f:
    f.write("Hi, I am learning how to write files using Python.\n")
    f.write("This will be the second line.\n")
    f.write("Third Line.\n")

with(open('output.txt', 'r')) as f:
    content = f.readlines()
    for line in content:
        print(line)

def count_words(path):
    total_words = 0
    with(open(path, 'r')) as f:
        lines = f.readlines()
        for line in lines:
            words =line.split()
            num_words = len(words)
            total_words += num_words

    return total_words

print(count_words('output.txt'))


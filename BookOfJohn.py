word_counts = {'Father': 0, 'God': 0, 'Christ': 0, 'Spirit': 0,'spirit': 0, 'life': 0, 'man': 0}

file = open('bookofjohn.txt', 'r')

for line in file:
    words = line.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1

for word, count in word_counts.items():
    print(f"{word}: {count}")
from collections import Counter

list = [1,2,3,2,1,1,3,1]

frecventa = Counter(list)
n = 2

print(frecventa.most_common(n))
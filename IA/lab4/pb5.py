from collections import Counter

list = [1,2,2,4,5,6,7,8,9]

frecventa = Counter(list)

print(frecventa)
print(frecventa.most_common(2))
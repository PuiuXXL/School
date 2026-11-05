def most_frequent(letters):
    dic = {}
    for char in letters:
        char = char.lower()
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    print(dic)

    max_char = []
    max_counts = 0
    for item in dic.keys():
        if dic[item] > max_counts:
            max_char.clear()
            max_counts = dic[item]
            max_char.append(item)
        elif dic[item] == max_counts:
            max_char.append(item)
   
    
    return max_char


def read_file(fileName):
    letters = []
    with open(fileName,"r") as f:
        for line in f:
            for word in line.split():
                letters.append(word)
   
    return letters







fileName = "letters.txt"
letters = read_file(fileName)
print(most_frequent(letters))
# print(most_frequent(letters))


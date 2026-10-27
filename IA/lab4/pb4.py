dic = {}
with open("file.txt","r") as f:
    for line in f:
        for word in line.split():
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1

print(dic)

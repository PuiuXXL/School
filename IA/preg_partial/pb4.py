def freq_counter(file_name):
    dic = {}

    with open(file_name,"r") as f:
        for line in f:
            for word in line.split():
                if word in dic.keys():
                    dic[word] += 1
                else:
                    dic[word] = 1
    return dic

print(freq_counter("file.txt"))

f = open("file1.txt","r")
g = open("file2.txt","w")

for line in f:
    # g.write(line.capitalize())
    # print(line[:-1])
    # for string in line:
    #     g.write(string.capitalize())
    #     print(string)
    words = line.split()
    for word in words:
        g.write(word.capitalize())
        g.write(" ")
    g.write("\n")
f.close()
g.close()
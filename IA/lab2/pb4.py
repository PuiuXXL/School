s_in = input("String: ")
num_in = int(input("Number: "))

dic = {}
for  num in range(num_in):
    dic[num] = 0

for index in range(min(num_in,len(s_in))):
    dic[index] = s_in[index]

print(dic)
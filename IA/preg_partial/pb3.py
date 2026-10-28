def func(array_a,array_b):
    for index1 in range(len(array_a) - 2):
        for index2 in range(len(array_b) - 2):
            if array_a[index1:index1 + 3] == array_b[index2: index2 + 3]:
                return True
    return False

a = [1, 10, 9, 10, 8]
b = [10, 8, 10, 7, 6]

print(func(a,b))
def consecutive_3(array_a, array_b):
    for i in range(len(array_a) - 2):
        for j in range(len(array_b) - 2):
            if array_a[i:i+3] == array_b[j:j+3]:
                return True
    return False

a = [1, 10, 9, 10, 8]
b = [10, 9, 10, 7, 6]

print(consecutive_3(a,b))
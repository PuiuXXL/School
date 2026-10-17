number = int(input())
if number % 2 == 0:
    for num in range(number):
        print(num)
else:
    for num in range(number):
        print(num*num)
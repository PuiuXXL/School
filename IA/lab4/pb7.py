list = [[1,2,3],[4,5,6]]

# new_list = []
# for item in list:
#     for num in item:
#         new_list.append(num)

new_list = [num for item in list for num in item]
print(new_list)
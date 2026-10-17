friends = [("andrew",10), ("george",20),("andrew",5),("ann",10)]

friends_set = set(element[0] for element in friends)
print(friends_set)
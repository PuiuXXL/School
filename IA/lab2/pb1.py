price =  {
    "apples" : 10,
    "milk" : 12,
    "bread" : 5
}

mylist = [("apples",2) , ("milk",2)]

total = sum(price[product] * size for product,size in mylist)

print(total)
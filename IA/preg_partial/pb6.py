a = [1,2,3]
b = ['a', 'b','c']

lista = zip(a,b)
res = list(lista)
for x,y in zip(a,b):
    print(f"{x}, '{y}'")
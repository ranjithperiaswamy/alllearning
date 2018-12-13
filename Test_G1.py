mylist=['Hello World']

for x in mylist:
    print(x)

print(list(x+x for x in mylist))

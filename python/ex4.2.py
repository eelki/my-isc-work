mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print(count, item)

first, middle, last = mylist
print(first, middle, last)

middle, last, first = first, middle, last
print(first, middle, last)

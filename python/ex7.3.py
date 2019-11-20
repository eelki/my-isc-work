import copy
a = [0, 1, 2]
b = copy.deepcopy(a)

print(a)
print(b)

b[0] = "hello"

print(a)
print(b)

forward = []
backward = []
values = ["a", "b", "c"]

for x in values:
    forward.append(x)
    backward.insert(0, x)

print(forward)
print(backward)

forward.reverse()

print(forward)
print(backward)

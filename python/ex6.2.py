s = "I love to write python"

split_s = s.split()

for word in split_s:
    if word.lower().find("i") > -1:
        print(f"I found i in: {word}")

for word in split_s:
    print(word.lower().find("i"))

band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}

for member in band:
    if member in counts:
        counts[member] += 1
    else:
        counts.setdefault(member, 1)
    
for (name, count) in counts.items():
    print(f"There are {count} people named {name} in the band")

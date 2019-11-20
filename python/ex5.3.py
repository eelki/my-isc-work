with open('weather.csv', 'r') as reader:
    header = reader.readline()
    rain = []
    for line in reader.readlines():
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)

print(rain)

with open("myrain.txt", 'w') as writer:
    for r in rain:    
        writer.write(str(r) + "\n")

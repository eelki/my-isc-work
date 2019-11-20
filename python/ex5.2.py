with open('weather.csv', 'r') as reader:
    data = reader.readline()
    while data != '':
        print(data)
        data = reader.readline()
    print("It's over!!!!")

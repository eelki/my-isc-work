gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0

while count < 4:
    for gas in gases:
        item = gas
        print(str(count) + ' - ' + item)
        count += 1

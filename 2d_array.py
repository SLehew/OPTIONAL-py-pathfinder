

x, y = [], []

with open('elevation_small.txt') as elevation_file:
    for line in elevation_file.readlines():
        row = line.split()
        x.append(row[0])
        y.append(row[1])

print(x[1], y[4])

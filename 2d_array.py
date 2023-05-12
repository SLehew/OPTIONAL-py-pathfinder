elevation_array = []

with open('elevation_small.txt') as file:
    main_list = file.readline()

    for line in main_list:
        point = line.split(' ')
        x = int(point[0])
        y = int(point[1])
        point_as_array = [x, y]
        elevation_array.append(point_as_array)

print(elevation_array)

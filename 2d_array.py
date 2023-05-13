elevation_array = []

with open("elevation_small.txt") as elevation_file:
    lines = elevation_file.readlines()
elevation_array = [l.strip().split(" ") for l in lines]


print()

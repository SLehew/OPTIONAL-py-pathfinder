from PIL import Image, ImageDraw
import numpy as np


# reading the data and converting to a 2D Array


def read_data(file):
    with open(file, 'r') as lines:
        lines = [line.strip() for line in lines]
        data = [[int(num) for num in line.split()]for line in lines]
        data = np.array(data)
    return data


elevations = read_data('elevation_small.txt')

# finds lowest elevation


def math(elevation_low_high_mean):

    lowest = np.min(elevation_low_high_mean)
    highest = np.max(elevation_low_high_mean)
    average = np.mean(elevation_low_high_mean)

    print(lowest, highest, average)
    return lowest, highest, average


math(elevations)

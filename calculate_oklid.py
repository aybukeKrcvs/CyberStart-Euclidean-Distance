import math

points = [(3,5), (1, 6), (9, 4), (-2, 3), (7, -6)]
distance = []

def euclideanDistance(points):
    for i in range(len(points) - 1):
        for k in range(i+1, len(points)):
            coord1 = points[i]
            coord2 = points[k]
            current_dist = math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)
            distance.append(current_dist)

def find_min_number(list):
    current_min = list[0]
    for i in range(1, len(list)):
        if list[i] < current_min:
            current_min = list[i]
    return current_min

euclideanDistance(points)
print(f"minimum distance between the points: {find_min_number(distance)}")
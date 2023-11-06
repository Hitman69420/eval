import math

def euclidean_distance(p1, p2):
    # Calculate the Euclidean distance between two points
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def brute_force_closest_pair(points):
    n = len(points)
    if n < 2:
        return None, None, float('inf')

    min_distance = float('inf')
    closest_pair = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair[0], closest_pair[1], min_distance

def closest_pair(points):
    n = len(points)

    if n <= 3:
        return brute_force_closest_pair(points)

    points.sort(key=lambda p: p[0])  # Sort points by x-coordinate

    mid = n // 2
    mid_point = points[mid]

    left_half = points[:mid]
    right_half = points[mid:]

    left_pair = closest_pair(left_half)
    right_pair = closest_pair(right_half)

    min_distance = min(left_pair[2], right_pair[2])

    strip = [point for point in points if abs(point[0] - mid_point[0]) < min_distance]

    strip_size = len(strip)

    for i in range(strip_size):
        j = i + 1
        while j < strip_size and (strip[j][1] - strip[i][1]) < min_distance:
            min_distance = min(min_distance, euclidean_distance(strip[i], strip[j]))
            j += 1

    if left_pair[2] < right_pair[2]:
        return left_pair
    else:
        return right_pair

# Example usage:
points = [(0, 0), (1, 2), (2, 3), (3, 4), (4, 5)]
result = closest_pair(points)
print("Closest pair:", result[0], result[1])
print("Minimum distance:", result[2])

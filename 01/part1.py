with open('input') as f:
    s = f.read()
lines = s.splitlines()
locations_left = list()
locations_right = list()
for line in lines:
    left, right = line.split("   ")
    left_i = int(left)
    right_i = int(right)
    locations_left.append(left_i)
    locations_right.append(right_i)
locations_left.sort()
locations_right.sort()
sorted_lines = dict(zip(locations_left, locations_right))
distances = list()
for left, right in sorted_lines.items():
    distance = left - right
    if distance < 0:
        distance = right - left
    distances.append(distance)
total_distance = sum(distances)
print(total_distance)

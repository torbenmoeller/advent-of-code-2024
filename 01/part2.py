from collections import Counter

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

val = Counter(locations_right)
scores = list()
for location in locations_left:
    score = val[location] * location
    scores.append(score)

print(sum(scores))
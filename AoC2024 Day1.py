from collections import Counter

side1 = []
side2 = []

with open("Day1.txt", "r") as file:
    for line in file:
        splitted = line.strip().split()
        side1.append(int(splitted[0]))
        side2.append(int(splitted[1]))

# If sorting is necessary for your application
side1.sort()
side2.sort()

# Calculate the sum of absolute differences
dif = sum(abs(a - b) for a, b in zip(side1, side2))
print(dif)

# Use Counter to count occurrences efficiently
side1_counter = Counter(side1)
side2_counter = Counter(side2)

# Calculate the score using the counters
score = sum(num * side1_counter[num] * side2_counter[num] for num in side1_counter)
print(score)

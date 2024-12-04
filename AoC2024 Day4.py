import re

with open("Day4.txt") as file:
    lines = [line.rstrip() for line in file]

counter = 0
# part 1
for i in range(len(lines)):
    counter += len(re.findall("XMAS", lines[i]))
    counter += len(re.findall("SAMX", lines[i]))
    for j in range(len(lines[i])):

        # Vertical check
        if i + 3 < len(lines):
            if all(len(lines[i + k]) > j for k in range(4)):
                word = ''.join(lines[i + k][j] for k in range(4))
                if word == "XMAS" or word == "SAMX":
                    counter += 1

        # Diagonal down-right check
        if i + 3 < len(lines) and j + 3 < len(lines[i]):
            if all(len(lines[i + k]) > j + k for k in range(4)):
                word = ''.join(lines[i + k][j + k] for k in range(4))
                if word == "XMAS" or word == "SAMX":
                    counter += 1

        # Diagonal down-left check
        if i + 3 < len(lines) and j - 3 >= 0:
            if all(len(lines[i + k]) > j - k >= 0 for k in range(4)):
                word = ''.join(lines[i + k][j - k] for k in range(4))
                if word == "XMAS" or word == "SAMX":
                    counter += 1

print(counter)

# part 2

counter = 0

rows = len(lines)
cols = len(lines[0])

mas_variants = {'MAS', 'SAM'}

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        center_char = lines[i][j]

        if center_char != 'A':
            continue

        diagonal1 = ""
        diagonal2 = ""

        if j + 1 < len(lines[i + 1]):
            diagonal1 = lines[i - 1][j - 1] + center_char + lines[i + 1][j + 1]
            diagonal2 = lines[i - 1][j + 1] + center_char + lines[i + 1][j - 1]

        if diagonal1 in mas_variants and diagonal2 in mas_variants:
            counter += 1

print(counter)

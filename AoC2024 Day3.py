import re

pattern = r"mul\(([0-9]{1,3},[0-9]{1,3})\)"
result = 0
with open("Day3.txt", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            result += (int(match.split(",")[0]) * int(match.split(",")[1]))

print(result)

pattern_do = re.compile(r"do\((\))")
pattern_dont = re.compile(r"don\'t\((\))")
pattern = re.compile(pattern)
result = 0
mul_enabled = True

with open("Day3.txt", "r") as file:
    for line in file:
        index = 0
        while index < len(line):
            match_dont = pattern_dont.match(line, index)
            if match_dont:
                mul_enabled = False
                index = match_dont.end()
                continue

            match_do = pattern_do.match(line, index)
            if match_do:
                mul_enabled = True
                index = match_do.end()
                continue

            match_mul = pattern.match(line, index)
            if match_mul:
                if mul_enabled:
                    matched = match_mul.group(1).split(",")

                    x = int(matched[0])
                    y = int(matched[1])
                    result += x * y
                index = match_mul.end()
                continue

            index += 1

print(result)

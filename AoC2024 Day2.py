def decreasing(numbers):
    return all(x <= y for x, y in zip(numbers, numbers[1:]))


def increasing(numbers):
    return all(x >= y for x, y in zip(numbers, numbers[1:]))


def range_validation(numbers):
    return all(1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))


def d2p1():
    counter = 0

    with open("Day2.txt", "r") as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))

            if not numbers:
                continue
            is_decreasing = decreasing(numbers)
            is_increasing = increasing(numbers)

            if is_decreasing or is_increasing:
                if range_validation(numbers):
                    counter += 1
    print(counter)


def d2p2():
    counter = 0

    with open("Day2.txt", "r") as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))

            if not numbers:
                continue

            is_decreasing = decreasing(numbers)
            is_increasing = increasing(numbers)

            if is_decreasing or is_increasing:
                if range_validation(numbers):
                    counter += 1
                else:
                    for i in range(len(numbers)):

                        numbers1 = numbers[:i] + numbers[i + 1:]
                        if range_validation(numbers1):
                            counter += 1
                            break

            else:
                for i in range(len(numbers)):
                    numbers1 = numbers[:i] + numbers[i + 1:]

                    is_decreasing = decreasing(numbers1)
                    is_increasing = increasing(numbers1)

                    if is_decreasing or is_increasing:
                        if range_validation(numbers1):
                            counter += 1
                            break

    print(counter)


d2p1()
d2p2()

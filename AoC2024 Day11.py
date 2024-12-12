from collections import Counter


def read_line():
    with open("Day11.txt", "r") as file:
        stones = file.read().split()
        return Counter(stone.strip() for stone in stones)


def process_stone(stone):

    if stone == "0":
        return ["1"]

    length = len(stone)
    if length % 2 == 0:
        half = length // 2
        left_half = stone[:half]
        right_half = stone[half:]

        def process_half(h):
            if set(h) == {"0"}:
                return "0"
            else:
                return h.lstrip("0") or "0"

        return [process_half(left_half), process_half(right_half)]

    else:
        num = int(stone)
        num_stone = num * 2024
        return [str(num_stone)]


def blink(stones_counter, n):

    current = stones_counter
    for _ in range(n):
        new_counter = Counter()
        for stone, count in current.items():
            results = process_stone(stone)
            for r in results:
                new_counter[r] += count
        current = new_counter
    return sum(current.values())


input_stones = read_line()
print(blink(input_stones, 25))
print(blink(input_stones, 75))

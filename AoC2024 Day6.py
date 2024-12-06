def turn_right(direction):
    # Direction: 0=up, 1=right, 2=down, 3=left
    return (direction + 1) % 4


def forward_position(x, y, direction):
    # direction: 0=up, 1=right, 2=down, 3=left
    if direction == 0:
        return x - 1, y
    elif direction == 1:
        return x, y + 1
    elif direction == 2:
        return x + 1, y
    elif direction == 3:
        return x, y - 1


def get_map():
    with open('Day6.txt', 'r') as f:
        return [list(line.rstrip('\n')) for line in f]


def is_loop(direction, rows, cols, lab, guard_x, guard_y):
    already_visited = False

    visited = set()
    visited.add((guard_x, guard_y, direction))

    while not already_visited:
        nx, ny = forward_position(guard_x, guard_y, direction)

        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            break
        if lab[nx][ny] == '#':
            direction = turn_right(direction)
            continue
        else:
            # Move forward
            guard_x, guard_y = nx, ny
            if (guard_x, guard_y, direction) in visited:
                already_visited = True
            else:
                visited.add((guard_x, guard_y, direction))

    return already_visited


def d6p1():
    lab = get_map()

    rows = len(lab)
    cols = len(lab[0]) if rows > 0 else 0

    directions_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    guard_x = guard_y = None
    direction = None

    for i in range(rows):
        for j in range(cols):
            if lab[i][j] in directions_map:
                guard_x, guard_y = i, j
                direction = directions_map[lab[i][j]]
                lab[i][j] = '.'
                break
        if guard_x is not None:
            break

    visited = set()
    visited.add((guard_x, guard_y))

    while True:
        nx, ny = forward_position(guard_x, guard_y, direction)

        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            break
        if lab[nx][ny] == '#':
            direction = turn_right(direction)
            continue
        else:
            # Move forward
            guard_x, guard_y = nx, ny
            visited.add((guard_x, guard_y))

    print(len(visited))


def d6p2():
    lab = get_map()
    rows = len(lab)
    cols = len(lab[0]) if rows > 0 else 0
    counter = 0

    directions_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    guard_x = guard_y = None
    direction = None

    for i in range(rows):
        for j in range(cols):
            if lab[i][j] in directions_map:
                guard_x, guard_y = i, j
                direction = directions_map[lab[i][j]]
                lab[i][j] = '.'
                break
        if guard_x is not None:
            break

    for i in range(rows):
        for j in range(cols):
            edited_lab = [row.copy() for row in lab]

            if edited_lab[i][j] != "#":
                edited_lab[i][j] = "#"
                if is_loop(direction, rows, cols, edited_lab, guard_x, guard_y):
                    counter += 1

    print(counter)


d6p1()
d6p2()

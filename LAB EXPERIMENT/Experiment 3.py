
from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            return path

        states = [
            (cap1, b), (a, cap2), (0, b), (a, 0),
            (a - min(a, cap2 - b), b + min(a, cap2 - b)),
            (a + min(b, cap1 - a), b - min(b, cap1 - a))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None

result = water_jug(4, 3, 2)

if result:
    for state in result:
        print("Jug 1:", state[0], "Jug 2:", state[1])
else:
    print("No solution")

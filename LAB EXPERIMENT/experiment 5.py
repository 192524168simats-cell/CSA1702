
from collections import deque
def valid(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    # Left bank
    if m > 0 and c > m:
        return False
    # Right bank
    mr, cr = 3 - m, 3 - c
    if mr > 0 and cr > mr:
        return False
    return True
def solve():
    start = (3, 3, 0)  # M, C, boat: 0=left, 1=right
    goal = (0, 0, 1)
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new_state = (m-dm, c-dc, 1)
            else:
                new_state = (m+dm, c+dc, 0)

            if (valid(new_state[0], new_state[1])
                    and new_state not in visited):
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

path = solve()

if path:
    for state in path:
        print("Missionaries:", state[0],
              "Cannibals:", state[1],
              "Boat:", "Right" if state[2] else "Left")
else:
    print("No solution")

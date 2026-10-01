from collections import deque

def solve_8_puzzle(start):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        # Up, Down, Left, Right index offsets
        moves = []
        if row > 0: moves.append(zero - 3)
        if row < 2: moves.append(zero + 3)
        if col > 0: moves.append(zero - 1)
        if col < 2: moves.append(zero + 1)

        for move in moves:
            # Swap blank space (0) with neighbor
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_tuple = tuple(new_state)

            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append((new_tuple, path + [new_tuple]))

# Example: 1 step away from solved
start_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
solution = solve_8_puzzle(start_state)

for step, board in enumerate(solution):
    print(f"Step {step}:")
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

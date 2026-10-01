from itertools import permutations

def solve_8_queens():
    for board in permutations(range(8)):
        if len(set(board[i] + i for i in range(8))) == 8 and \
           len(set(board[i] - i for i in range(8))) == 8:
            return board

solution = solve_8_queens()

for row in range(8):
    print(" ".join("Q" if solution[col] == row else "." for col in range(8)))


N = 8
board = [-1] * N

def safe(row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    for r in range(N):
        for c in range(N):
            print("Q" if board[r] == c else ".", end=" ")
        print()
else:
    print("No solution")

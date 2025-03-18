# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

N = 9
EMPTY_CHAR = '-'
x = 0

def check(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solve(board, row, col):
    global x
    x += 1
    # rec stop condition
    if row == N - 1 and col == N:
        return True

    if col == N:  # when we need to go to the next row
        row += 1
        col = 0

    if board[row][col] != EMPTY_CHAR:  # if cell is filled, move to the next cell
        return solve(board, row, col + 1)
    for num in range(1, N + 1, 1):  # run over all options
        if check_location_is_safe(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
        board[row][col] = EMPTY_CHAR
    return False

def print_board(board):
    for i in range(N):
        if i % 3 == 0 or i == 9:
            print("-" * 25)
        for j in range(N):
            char = ""
            if j % 3 == 0:
                char += "| "
            char += str(board[i][j])
            if j == 8:
                char += " |"
            print(char, end=" ")
        print()
        if i == 8:
            print("-" * 25)

def get_new_board():
    # 0 means unassigned cells
    grid = [[3, "-", 6, 5, "-", 8, 4, "-", "-"],
            [5, 2, "-", "-", "-", "-", "-", "-", "-"],
            ["-", 8, 7, "-", "-", "-", "-", 3, 1],
            ["-", "-", 3, "-", 1, "-", "-", 8, "-"],
            [9, "-", "-", 8, 6, 3, "-", "-", 5],
            ["-", 5, "-", "-", 9, "-", 6, "-", "-"],
            [1, 3, "-", "-", "-", "-", 2, 5, "-"],
            ["-", "-", "-", "-", "-", "-", "-", 7, 4],
            ["-", "-", 5, 2, "-", 6, 3, "-", "-"]]
    return grid

def check_location_is_safe(arr, row, col, num):
    # Check if 'num' is not already
    # placed in current row,
    # current column and current 3x3 box
    res = not used_in_row(arr, row, col, num) and not used_in_col(arr, row, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)
    return res

def run(board):
    print_board(board)
    if solve(board, 0 ,0):
        print(x)
        print_board(board)

        return board
    else:
        print("no solution")
        return None


    ## fill possability

def used_in_row(board, row, col, num):
    for i in range(N):
        if board[row][i] and i != col:
            if board[row][i] == num:
                return True
    return False

def used_in_col(board, row, col, num):
    for i in range(N):
        if board[i][col] and i != row:
            if board[i][col] == num:
                return True
    return False

def used_in_box(board, row, col, num):
    sqrt_N = int(math.sqrt(N))
    for i in range(sqrt_N):
        for j in range(sqrt_N):
            if(board[i + row][j + col] == num):
                return True
    return False



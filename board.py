from cell import Cell

class Board:
  def __init__(self, n, board):
    self.n = n
    self.board = self.init_board(board)



  def init_board(self, board):
    t = [[0] * self.n for i in range(self.n)]
    for i in range(self.n):
      for j in range(self.n):
        cell = Cell(i, j, board[i][j])
        t[i][j] = cell
    return t


## need to fix this function to handle other types of boards sizes
  def print_board(self):
    for i in range(self.n):
      if i % 3 == 0 or i == 9:
        print("-" * 25)
      for j in range(self.n):
        char = ""
        if j % 3 == 0:
          char += "| "
        char += str((self.board[i][j]).val)
        if j == 8:
          char += " |"
        print(char, end=" ")
      print()
      if i == 8:
        print("-" * 25)

  def print_all_possibilities(self):
    for i in range(self.n):
      for j in range(self.n):
        if len(self.board[i][j].possibilities) > 0:
         print('({0},{1}): {2} '.format(i, j, self.board[i][j].possibilities))

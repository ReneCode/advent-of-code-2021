
# https://adventofcode.com/2021/day/13

import util



def read_data():
  lines = util.read_data('./13.data')
  dots = []
  folds = []

  read_dots = True
  for line in lines:
    if line == '':
      read_dots = False
    else:
      if read_dots:
        [x,y] = line.split(",")
        dots.append((int(x),int(y)))
      else:
        tok = line.split(' ')
        [axis, nr] = tok[2].split('=')
        folds.append((axis, int(nr)))

  max_x = 0
  max_y = 0
  for dot in dots:
    max_x = max(max_x, dot[0])
    max_y = max(max_y, dot[1])

  board = []
  for y in range(max_y+1):
    row = [False] * (max_x +1)
    board.append(row)

  for dot in dots:
    (x,y) = dot
    board[y][x] = True

  return (board, folds)


def debug(board):
  cnt = 0
  for row in board:
    line = ''
    for v in row:
      if v:
        line = line + "#"
        cnt = cnt +1
      else:
        line = line + "."
    print(line)
  print(f'count:{cnt}')

def fold_x(board, x_fold):
  old_x_max = len(board[0])
  new_board = []
  for row in board:
    check = row[x_fold]
    if check:
      raise Exception(f'val on fold line {x_fold} not empty')
    new_row = [False] * x_fold
    dx = 1
    while x_fold + dx < old_x_max:
      left = row[x_fold -dx]
      right = row[x_fold +dx]
      result = left or right
      new_row[x_fold -dx] = result
      dx = dx+1
    new_board.append(new_row)
  return new_board


def merge_rows(row_a, row_b):
  result = []
  for i in range(len(row_a)):
    val = row_a[i] or row_b[i]
    result.append(val)
  return result

def fold_y(board, y_fold):
  old_y_max = len(board)
  # y_max = old_y_max // 2
  # if y_max != y_fold:
  #   raise Exception(f'fold_y {y_fold} but calc {y_max}')
  new_board = []
  for y in range(y_fold):
    row_top = board[y]
    row_bottom = board[old_y_max -1 -y]
    row_result = merge_rows(row_top, row_bottom)
    new_board.append(row_result)
  return new_board



(board, folds) = read_data()
debug(board)

for fold in folds:
  print(f'--- fold {fold[0]} {fold[1]}')
  if fold[0] == 'x':
    board = fold_x(board, fold[1])
  else:
    board = fold_y(board, fold[1])
  debug(board)
  exit()
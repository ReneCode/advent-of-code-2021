
# https://adventofcode.com/2021/day/9

import util

MAX_NR = 9

def read_data():
  lines = util.read_data('./9.data')
  result = []
  for line in lines:
    row = [int(c) for c in line]
    result.append(row)
  return result


def get_low_index_in_row(row):
  xlen = len(row)
  result = []
  for x in range(xlen):
    nr = row[x]
    left = MAX_NR
    right = MAX_NR
    if x > 0:
      left = row[x-1]
    if x+1 < xlen:
      right = row[x+1]
    if left > nr and right > nr:
      result.append(x)
  return result


def get_low_points(board):
  xlen = len(board[0])
  ylen = len(board)
  result_coords = []
  for y in range(ylen):
    indicies = get_low_index_in_row(board[y])
    for x in indicies:
      up = MAX_NR
      down = MAX_NR
      nr = board[y][x]
      if y > 0:
        up = board[y-1][x]
      if y+1 < ylen:
        down = board[y+1][x]
      if up > nr and down > nr:
        result_coords.append( (x, y) )
  return result_coords

def get_values(board, coords):
  result = []
  for coord in coords:
    (x,y) = coord
    result.append(board[y][x])
  return result

board = read_data()
low_coords = get_low_points(board)
result = get_values(board, low_coords)
risk_level = [n+1 for n in result]
result_sum = sum(risk_level)

print(board)
print(low_coords)
print(result)
print(result_sum)

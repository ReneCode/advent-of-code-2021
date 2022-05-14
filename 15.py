
# https://adventofcode.com/2021/day/15

import util

def read_data():
  board = []
  lines = util.read_data('./15-example-2.data')
  for line in lines:
    row = [int(n) for n in line]
    board.append(row)
  return board

def calc_shape(board):
  return (len(board[0]), len(board))


def get_next_pts(pt, board):
  (xlen, ylen) = calc_shape(board)
  pts = []
  (x,y) = pt
  if x > 0:
    pts.append((x-1,y))
  if y > 0:
    pts.append((x,y-1))
  if x+1 < xlen:
    pts.append((x+1,y))
  if y+1 < ylen:
    pts.append((x,y+1))
  return pts

def step(ways, way, board, end_pt):
  pt = way[-1]
  if pt == end_pt:
    ways.append(way)
    print(len(ways))
    return

  next_pts = get_next_pts(pt, board)
  for next_pt in next_pts:
    if not next_pt in way:
      w = way.copy()
      w.append(next_pt)
      step(ways, w, board, end_pt)



board = read_data()
(xlen, ylen) = calc_shape(board)

start_pt = (0,0)
end_pt = (xlen-1, ylen-1)
ways = []
way = [start_pt]

step(ways, way, board, end_pt)
# print(ways)

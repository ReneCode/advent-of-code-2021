
from util import read_data

# def read_data(filename):
#   input_data = []
#   with open(filename) as f:
#       lines = f.readlines()
#       input_data = [l.strip() for l in lines]
#   return input_data


def parse_lines(lines):
  cmds = []
  for line in lines:
    coords = line.split("->")
    start_coord = [int(n) for n in coords[0].split(",")]
    end_coord = [int(n) for n in coords[1].split(",")]
    cmds.append([start_coord, end_coord])
  return cmds

def remove_diagonal(cmds):
  result = []
  for cmd in cmds:
    start = cmd[0]
    end = cmd[1]
    if start[0] == end[0] or start[1] == end[1]:
      result.append(cmd)
  return result

def get_max_dimension(cmds):
  max_x = 0
  max_y = 0
  for cmd in cmds:
    start = cmd[0]
    end = cmd[1]
    max_x = max(max_x, start[0])
    max_x = max(max_x, end[0])
    max_y = max(max_y, start[1])
    max_y = max(max_y, end[1])
  return (max_x, max_y)

def debug_board(board):
  for row in board:
    vals = [str(n) for n in row]
    
    line = "".join(vals)
    line = line.replace("0", ".")
    print(line)

def add_cmd(board, cmd):
  [x0, y0] = cmd[0]
  [x1, y1] = cmd[1]
  board[y0][x0] = board[y0][x0] + 1
  board[y1][x1] = board[y1][x1] + 1


# advent_of_code_2021/5-example.data
input_data = read_data('./advent_of_code_2021/5-example.data')
cmds = parse_lines(input_data)
cmds = remove_diagonal(cmds)
(max_x, max_y) = get_max_dimension(cmds)
board = [ [0]*(max_x+1) for _ in range(max_y+1) ]


for cmd in cmds:
  add_cmd(board, cmd)

print(cmds)
debug_board(board)



example=result ="""
  0123456789
0 .......1..
1 ..1....1..
2 ..1....1..
3 .......1..
4 .112111211
5 ..........
6 ..........
7 ..........
8 ..........
9 222111....
"""
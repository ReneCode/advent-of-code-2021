
# https://adventofcode.com/2021/day/20

import util

LIGHT_ON = "#"
LIGHT_OFF = "."

class Image:
  def __init__(self, lines):
    self.positions = {}
    self.col_min = 0
    self.col_max = len(lines[0])-1
    self.row_min = 0
    self.row_max = len(lines)-1
    for row,image_line in enumerate(lines):
      for col,val in enumerate(lines):
        if val == LIGHT_ON:
          pos = (col,row)
          self.positions[pos] = True



def read_data(filename):
  lines = util.read_data(filename)
  algo_line = ""
  image_lines = []
  read_algo = True
  for line in lines:
    if line == "":
      read_algo = False
    else:
      if read_algo:
        algo_line = algo_line + line
      else:
        image_lines.append(line)
  # dict for algo
  algo = {}
  for i,val in enumerate(algo_line):
    if val == '#':
      algo[i] = True
    else:
      algo[i] = False

  # store image in position-dict
  image = {}
  for row,image_line in enumerate(image_lines):
    for col,val in enumerate(image_line):
      if val == LIGHT_ON:
        pos = (col,row)
        image[pos] = True
  return (algo, image)

def get_image_boundary(image):
  col_min = 0
  col_max = 0
  row_min = 0
  row_max = 0
  for pos in image:
    (col, row) = pos
    col_min = min(col_min, col)
    col_max = max(col_max, col)
    row_min = min(row_min, row)
    row_max = max(row_max, row)
  return (col_min, col_max, row_min, row_max)

def output(image):
  print('------------')
  (col_min, col_max, row_min, row_max) = get_image_boundary(image)
  count_on = 0
  border = 0
  for row in range(row_min-border, row_max+1 + border):
    line = ""
    for col in range(col_min-border, col_max+1 + border):
      pos = (col, row)
      if image.get(pos):
        line = line + LIGHT_ON
        count_on = count_on + 1
      else:
        line = line + LIGHT_OFF
    print(line)
  return count_on

def get_bit_val(image, col, row):
  bits = ""
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      pos = (c, r)
      bit = "0"
      if image.get(pos):
        bit = "1"
      bits = bits + bit
  val = int(bits, 2)
  return val

def calc(image, algo):
  (col_min, col_max, row_min, row_max) = get_image_boundary(image)
  border = 5
  result = {}
  for row in range(row_min-border, row_max+1 +border):
    for col in range(col_min-border, col_max+1 +border):
      bit_val = get_bit_val(image, col, row)
      if algo[bit_val]:
        result_pos = (col, row)
        result[result_pos] = True
  return result

(algo, image) = read_data('./20.data')
# print(algo)
output(image)
image = calc(image, algo)
output(image)
image = calc(image, algo)
count = output(image)
print(f'pixels on: {count}')



# https://adventofcode.com/2021/day/20

import util

LIGHT_ON = "#"
LIGHT_OFF = "."

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
  # add two 'lines' around the image
  width = len(image_lines[0])
  # top_bottom_line = "".join(['.']*(width+4))
  # image = []
  # image.append(top_bottom_line)
  # image.append(top_bottom_line)
  # for line in image_lines:
  #   enlarged_line = ".." + line + ".."
  #   image.append(enlarged_line)
  # image.append(top_bottom_line)
  # image.append(top_bottom_line)
    
  return (algo, image_lines)


def output(image):
  print('------------')
  for line in image:
    print(line)

def get_bit_val(image, col, row):
  max_x = len(image[0])
  max_y = len(image)
  # calculating the image'border' results 0
  # if col < 2 or row < 2:
  #   return 0
  # if (col+2) >= max_y:
  #   return 0
  # if (row+2) >= max_x:
  #   return 0
  
  bits = ""
  for r in range(row-1, row+2):
    for c in range(col-1, col+2):
      if r < 0 or c < 0 or r >= max_y or c >= max_x:
        bits = bits + "0"
      else:
        bit = "0"
        if image[r][c] == LIGHT_ON:
          bit = "1"
        bits = bits + bit
  val = int(bits, 2)
  return val

def calc(image, algo):
  result = []
  for row, line in enumerate(image):
    result_line = ""
    for col, w in enumerate(line):
      bit_val = get_bit_val(image, col, row)
      if algo[bit_val]:
        result_line = result_line + LIGHT_ON
      else:
        result_line = result_line + LIGHT_OFF
    result.append(result_line)
  return result

(algo, image) = read_data('./20-example.data')
print(algo)
output(image)
image = calc(image, algo)
output(image)


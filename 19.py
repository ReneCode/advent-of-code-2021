
# https://adventofcode.com/2021/day/19

import util

# return p1 - p2
def pos_sub(p1, p2):
  return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])


class Scanner:
  def __repr__(self):
    return f'{self.nr} / {self.positions}'

  def __init__(self, nr, positions):
    self.nr = nr
    self.positions = positions

  def calc_deltas(self, idx_pt):
    deltas = []
    rel_pt = self.positions[idx_pt]
    for i in range(len(self.positions)):
      if i != idx_pt:
        delta = pos_sub(self.positions[i], rel_pt)
        deltas.append(delta)
    return deltas

def read_data(filename):
  lines = util.read_data(filename)
  scanners = []
  scanner_nr = None
  positions = []
  for line in lines:
    if line.startswith('--- scanner '):
      tok = line.split(' ')
      scanner_nr = int(tok[2])
    elif line == '':
      scanner = Scanner(scanner_nr, positions)
      scanners.append(scanner)
      positions = []
      scanner_nr = None
    else:
      tokens = line.split(',')
      xyz = [int(n) for n in tokens]
      positions.append(tuple(xyz))
  if len(positions) > 0:
    scanner = Scanner(scanner_nr, positions)
    scanners.append(scanner)
  return scanners


def is_good_fit(vectors_a, vectors_b):
  count = 0
  minimum_count = 12-1  # 12 points => 11 deltas
  for vec_a in vectors_a:
    if vec_a in vectors_b:
      count = count +1
      if count >= minimum_count:
        return True
  return False

def sign(val):
  if val > 0:
    return 1
  if val < 0:
    return -1
  return 0

# mapping (2, -3, 1)
# => map (x,y,z) => (y,-z,x)
def map_vec(vec, mapping):
  x_idx = abs(mapping[0])-1
  y_idx = abs(mapping[1])-1
  z_idx = abs(mapping[2])-1
  x_sgn = sign(mapping[0])
  y_sgn = sign(mapping[1])
  z_sgn = sign(mapping[2])
  return (vec[x_idx]*x_sgn, vec[y_idx]*y_sgn, vec[z_idx]*z_sgn)


def get_all_mappings():
  bases = [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
  result = []
  for base in bases:
    for i in range(8):
      binary = format(i, '>03b')
      mapping = []
      for idx in range(3):
        if binary[idx] == '1':
          mapping.append(-base[idx])
        else:
          mapping.append(base[idx])
      result.append(tuple(mapping))
  return result


def find_similar_pos(scanner_a, scanner_b, all_mappings):


  for idx_a in range(len(scanner_a.positions)):
    deltas_a = scanner_a.calc_deltas(idx_a)
    for idx_b in range(len(scanner_b.positions)):
      deltas_b = scanner_b.calc_deltas(idx_b)
      for mapping in all_mappings:
        mapped_deltas_a = [map_vec(vec, mapping) for vec in deltas_a]
        found = is_good_fit(mapped_deltas_a, deltas_b)
        if found:
          vec_a = scanner_a.positions[idx_a]
          mapped_vec_a = map_vec(vec_a, mapping)
          vec_b = scanner_b.positions[idx_b]
          relative = pos_sub(vec_b, mapped_vec_a)
          print(f'found {idx_a} {vec_a}, {idx_b} {vec_b} mapping:{mapping} relative:{relative}')
          break


scanners = read_data('./19-example.data')
s1 = scanners[0]
s2 = scanners[1]
all_mappings = get_all_mappings()
find_similar_pos(s1, s2, all_mappings)


 
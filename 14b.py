
# https://adventofcode.com/2021/day/14

import util

def read_data():
  lines = util.read_data('./14-example.data')
  start = ''
  rules = {}
  for line in lines:
    if start == '':
      start = line
    elif line != '':
      [match, insert] = line.split(' -> ')
      rules[match] = insert
  return (start, rules)

class Polymer:
  def __repr__(self):
    result = f'{self.name} - {self.generations}/{self.char_counts}'
    return result


  def __init__(self, name):
    self.name = name
    self.generations = [] # string for each generation
    self.char_counts = [] # {} for each generation

  def calc_generations(self, cnt, rules):
    self.generations = []
    for i in range(cnt):
      polymer = self.name
      if i>0:
        polymer = self.generations[i-1]
      result = step(polymer, rules)
      self.generations.append(result)
      counts = get_char_counts(polymer)
      self.char_counts.append(counts)



def step(polymer, rules):
  result = ''
  poly_len = len(polymer)
  for i in range(poly_len-1):
    pair = polymer[i:i+2]
    result = result + pair[0]
    insert = rules.get(pair)
    if insert != None:
      result = result + insert
  result = result + polymer[-1]
  return result


def get_char_counts(polymer):
  counts = {}
  for w in polymer:
    val = counts.get(w)
    if val == None:
      counts[w] = 1
    else:
      counts[w] = val +1
  return counts

def calc_score(polymer):
  stats = {}
  for w in polymer:
    val = stats.get(w)
    if val == None:
      stats[w] = 1
    else:
      stats[w] = val +1
  min_cnt = None
  max_cnt = None
  for item in stats.items():
    (_, cnt) = item
    if min_cnt == None:
      min_cnt = cnt
    else:
      min_cnt = min(min_cnt, cnt)
    if max_cnt == None:
      max_cnt = cnt
    else:
      max_cnt = max(max_cnt, cnt)
  return max_cnt - min_cnt



def polymer_to_pairs(polymer):
  l = len(polymer)
  pairs = []
  for i in range(l-1):
    s = polymer[i:i+2]
    pairs.append(s)
  return pairs


# def traverse(target_len, pair, tree, result, depth):
#   if target_len == depth:
#     result.append(pair[0])
#     pass
#   else:
#     (left,right) = tree[pair]
#     traverse(target_len, left, tree, result, depth+1)
#     traverse(target_len, right, tree, result, depth+1)


(start_polymer, rules) = read_data()
start_polymer = 'CB'

polymers = {}
for rule in rules:
  polymer = Polymer(rule)
  polymer.calc_generations(5, rules)
  polymers[rule] = polymer

print(polymers)



# rule = CB -> H
#
# key = 'CB'  value = (CH,HB)
# tree = {}
# for key,value in rules.items():
#   left = key[0] + value
#   right = value + key[1]
#   tree[key] = (left, right)

# print(tree)
# pairs = polymer_to_pairs(polymer)
# print(pairs)

# result = []
# steps = 3
# for pair in pairs:
#   traverse(steps, pair, tree, result, 0)
# result.append(pair[-1])

# finish_polymer = ''.join(result)
# print(finish_polymer)
# score = calc_score(finish_polymer)
# print(f'score:{score}')



# for i in range(10):
#   polymer = step(polymer, rules)
# score = calc_score(polymer)
# print(f'After step {i+1}: {polymer[0:10]} {len(polymer)} {score}')

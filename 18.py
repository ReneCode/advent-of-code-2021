
# https://adventofcode.com/2021/day/18

import util

def is_int(obj):
  return isinstance(obj, int)


def pair_to_array(pair):
  items = []
  for w in pair:
    if w == '[' or w == ']':
      items.append(w)
    elif w == ',':
      items.append(w)
    else:
      items.append(int(w))
  return items

def array_to_pair(items):
  result = ''
  last_item = None
  for item in items:
    if item == '[' or item == ']' or item == ',':
      result = result + item
    else:
      result = result + str(item)
  return result
# 123[4,5]67  =>  123067
def get_and_clear_pair(pair, idx):
  left = None
  right = None
  item = pair.pop(idx)
  assert(item == '[')
  left = pair.pop(idx)
  item = pair.pop(idx)
  right = pair.pop(idx)
  pair[idx] = 0
  return (left, right)


def add_next_int(result, val, idx, delta_idx):
  i = idx + delta_idx
  while i>= 0 and i < len(result):
    if is_int(result[i]):
      result[i] = result[i] + val
      return
    i = i + delta_idx

def explode(items):
  count_open_brackets = 0
  ignore_until_bracket_close = False
  for idx, item in enumerate(items):
    if item == '[':
      count_open_brackets = count_open_brackets +1
      if count_open_brackets > 4:
        (left, right) = get_and_clear_pair(items, idx)
        add_next_int(items, left, idx, -1)
        add_next_int(items, right, idx, +1)
        return True
    elif item == ']':
      count_open_brackets = count_open_brackets -1
  return False

def insert_pair(items, idx, left, right):
  items.pop(idx)
  items.insert(idx, '[')
  items.insert(idx+1, left)
  items.insert(idx+2, ',')
  items.insert(idx+3, right)
  items.insert(idx+4, ']')


def split(items):
  for idx, item in enumerate(items):
    if is_int(item):
      if item >= 10:
        left = right = item // 2
        if item % 2 > 0:
          right = right + 1
        insert_pair(items, idx, left, right)
        return True
  return False


def reduce(pair):
  items = pair_to_array(pair)
  cont = True
  while cont:
    while explode(items):
      pass
    cont = split(items)

  pair = array_to_pair(items)
  return pair

def add(p1, p2):
  pair = f'[{p1},{p2}]'

  pair = reduce(pair)
  return pair

def add_all(pairs):
  result = pairs[0]
  for i in range(1, len(pairs)):
    result = add(result, pairs[i])
  return result



lines = util.read_data('./18-example.data')
result = add_all(lines)
print(result)


pair = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
result = reduce(pair)
# print(result)

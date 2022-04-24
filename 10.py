
# https://adventofcode.com/2021/day/10

import util

BRACKETS = [
  ('(', ')', 3),
  ('[', ']', 57),
  ('{', '}', 1197),
  ('<', '>', 25137)
]


class Stack:
  def __init__(self):
    self.values = []

  def push(self, val):
    pass


def is_open_bracket(c):
  for bracket in BRACKETS:
    if c == bracket[0]:
      return True
  return None

def is_close_bracket(c):
  for bracket in BRACKETS:
    if c == bracket[1]:
      return True
  return None

def get_close_bracket(open_bracket):
  for bracket in BRACKETS:
    if open_bracket == bracket[0]:
      return bracket[1]
  return None

def check_line(line):
  open_brackets = []
  for c in line:
    if is_open_bracket(c):
      open_brackets.append(c)
    else:
      if len(open_brackets) > 0:
        need_close_bracket = get_close_bracket(open_brackets[-1])
        if need_close_bracket != c:
          print(f'{line} - Expected {need_close_bracket} but found {c}')
          return c
        else:
          open_brackets.pop()
      else:
        print(f'found {c} but there was no open bracket before')
        return c
  return None

def get_bad_char_value(c):
  for bracket in BRACKETS:
    if c == bracket[0] or c == bracket[1]:
      return bracket[2]
  return 0

def part_1():
  lines = util.read_data('./10.data')
  total_error_score = 0
  for line in lines:
    bad_char = check_line(line)
    if bad_char != None:
      val = get_bad_char_value(bad_char)
      total_error_score = total_error_score + val
  print(f'Result: {total_error_score}')

part_1()
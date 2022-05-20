
# https://adventofcode.com/2021/day/15

import util
import random

def read_data():
  board = []
  lines = util.read_data('./15.data')
  for line in lines:
    row = [int(n) for n in line]
    board.append(row)
  return board



class Way:
  def __init__(self):
    self.points = []


  




class WayFinder:
  def __init__(self, board):
    self.ways = []
    self.visited_points = {}
    self.board = board
    (xlen, ylen) = self.calc_shape()
    self.start_pt = (0,0)
    self.end_pt = (xlen-1, ylen-1)

  def calc_all_ways(self):
    pt = self.start_pt
    way = []
    # self.init_visited_points()
    self.step(way, self.start_pt)
    return self.ways

  def get_risk(self, pt):
    if pt == self.start_pt:
      return 0
    (x,y) = pt
    return self.board[y][x]

  def calc_shape(self):
    return (len(self.board[0]), len(self.board))

  def get_visited_risk(self,pt):
    return self.visited_points[pt]

  def get_bottom_right_points(self, pt):
    (x, y) = pt
    (xe, ye) = self.end_pt
    points = []
    if x < xe:
      points.append((x+1, y))
    if y < ye:
      points.append((x, y+1))
    return points

  def get_top_left_visited_risk(self, pt):
    (x,y) = pt
    result = []
    if x > 0:
      result.append((x-1,y))
    if y > 0:
      result.append((x, y-1))
    if len(result) == 0:
      return 0
    if len(result) == 1:
      return self.get_visited_risk(result[0])
    risk_a = self.get_visited_risk(result[0])
    risk_b = self.get_visited_risk(result[1])
    return min(risk_a, risk_b)

  def init_visited_points(self):
    (xlen, ylen) = self.calc_shape()
    self.visited_points[self.start_pt] = 0
    for x in range(xlen):
      for y in range(ylen):
        pt = (x,y)
        top_left_risk = self.get_top_left_visited_risk(pt)
        my_risk = self.get_risk(pt)
        self.visited_points[pt] = top_left_risk + my_risk +1


  def get_next_points(self, pt):
    (xlen, ylen) = self.calc_shape()
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

  def out_way(self, way):
    (xlen, ylen) = self.calc_shape()
    print('-------------------')
    for y in range(ylen):
      line = ''
      for x in range(xlen):
        pt = (x,y)
        if pt in way:
          line = line + '#'
        else:
          line = line + '.'
      print(line)

  def step(self, way, pt):
    way.append(pt)
    if pt == self.end_pt:
      self.ways.append(way.copy())
      # self.out_way(way)
      return
    next_pts = self.get_bottom_right_points(pt)
    for next_pt in next_pts:
      if not next_pt in way:
        self.step(way.copy(), next_pt)

  def calc_risk(self, way):
    total_risk = 0
    for pt in way:
      risk = self.get_risk(pt)
      total_risk = total_risk + risk
    return total_risk

  def calc_min_risk_of_all_ways(self):
    min_risk = None
    min_way = None
    for way in self.ways:
      total_risk = self.calc_risk(way)
      if min_risk == None or (total_risk < min_risk):
        min_risk = total_risk
        min_way = way
    return (min_risk, min_way)





board = read_data()
way_finder = WayFinder(board)
ways = way_finder.calc_all_ways()
(min_risk, min_way) = way_finder.calc_min_risk_of_all_ways()
print(len(ways))
way_finder.out_way(min_way)
print(min_risk)
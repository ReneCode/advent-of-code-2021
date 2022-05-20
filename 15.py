
# https://adventofcode.com/2021/day/15

import sys
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
  def __init__(self, points):
    self.points = points


  




class WayFinder:
  def __init__(self, board):
    self.ways = []
    self.visited_risk = {}
    self.board = board
    (xlen, ylen) = self.calc_shape()
    self.start_pt = (0,0)
    self.end_pt = (xlen-1, ylen-1)

  # def calc_all_ways(self):
  #   pt = self.start_pt
  #   way = []
  #   self.step(way, self.start_pt)
  #   return self.ways

  def get_risk(self, pt):
    if pt == self.start_pt:
      return 0
    (x,y) = pt
    return self.board[y][x]

  def calc_shape(self):
    return (len(self.board[0]), len(self.board))

  def get_visited_risk(self,pt):
    return self.visited_risk.get(pt)

  def set_visited_risk(self, pt, risk):
    existing_risk = self.visited_risk.get(pt)
    if existing_risk != None and risk >= existing_risk:
      raise Exception(f'risk on point {pt} alleady set {existing_risk}. Do not override with {risk}')
    self.visited_risk[pt] = risk

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



  def enter(self, points, pt, total_risk):
    if pt in points:
      return
    total_risk = total_risk + self.get_risk(pt)
    risk = self.get_visited_risk(pt)
    if risk != None:
      if total_risk >= risk:
        # not better -> stop
        return
    self.set_visited_risk(pt, total_risk)
    points.append(pt)
    if pt == self.end_pt:
      self.ways.append(points.copy())
      print(len(self.ways))
      self.out_way(points)
      return
    # next_points = self.get_bottom_right_points(pt)
    next_points = self.get_next_points(pt)

    for p in next_points:
      self.enter(points.copy(), p, total_risk)


  def calc_first_way(self):
    points = []
    self.enter(points, self.start_pt, 0)



  def init_visited_risk(self):
    (xlen, ylen) = self.calc_shape()
    for x in range(xlen):
      for y in range(ylen):
        pt = (x,y)
        top_left_risk = self.get_top_left_visited_risk(pt)
        my_risk = self.get_risk(pt)
        my_visited_risk = self.get_visited_risk(pt)
        total_risk = top_left_risk + my_risk + 1
        self.set_visited_risk(pt, total_risk)


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

  # def step(self, way, pt):
  #   way.append(pt)
  #   if pt == self.end_pt:
  #     self.ways.append(way.copy())
  #     # self.out_way(way)
  #     return
  #   next_pts = self.get_bottom_right_points(pt)
  #   for next_pt in next_pts:
  #     if not next_pt in way:
  #       self.step(way.copy(), next_pt)

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



sys.setrecursionlimit(10000+100)

board = read_data()
way_finder = WayFinder(board)
way_finder.init_visited_risk()
way_finder.calc_first_way()
# ways = way_finder.calc_all_ways()
(min_risk, min_way) = way_finder.calc_min_risk_of_all_ways()
way_finder.out_way(min_way)
print(len(way_finder.ways), min_risk)
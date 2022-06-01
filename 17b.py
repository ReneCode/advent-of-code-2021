
# https://adventofcode.com/2021/day/17



def read_target(line):
  tok = line.split(":")
  xy = tok[1].split(",")
  xvals = xy[0].split("=")[1]
  yvals = xy[1].split("=")[1]
  [x1,x2] = xvals.split("..")
  [y1,y2] = yvals.split("..")
  x1 = int(x1)
  x2 = int(x2)
  y1 = int(y1)
  y2 = int(y2)
  return ( (min(x1,x2), min(y1,y2)), (max(x1,x2), max(y1,y2)) )


def calc_velocity_x(target_left):
  sum = 0
  i = 0
  while sum < target_left:
    i = i+1
    sum = sum + i
  return i


def is_below(pta, ptb):
  return pta[0] < ptb[0]

def add_pt(pta, ptb):
  return (pta[0] + ptb[0], pta[1] + ptb[1])

def is_inside(pt, bottom_left, top_right):
  if pt[0] < bottom_left[0]:
    return False
  if pt[0] > top_right[0]:
    return False
  if pt[1] < bottom_left[1]:
    return False
  if pt[1] > top_right[1]:
    return False
  # print(f'pt inside:{pt}')
  return True

def next_vel(vel):
  (dx, dy) = vel
  dy = dy -1
  if dx > 0:
    dx = dx -1
  elif dx < 0:
    dx = dx +1
  else:
    dx = 0
  return (dx, dy)


def calc_trajectory(start_pt, start_vel, target):
  (target_bottom_left, target_top_right) = (target[0], target[1])
  pt = start_pt
  vel = start_vel
  trajectrory = [pt]
  while pt[1] >= target_bottom_left[1]:
    pt = add_pt(pt, vel)
    vel = next_vel(vel)
    # print(pt)
    trajectrory.append(pt)
    if is_inside(pt, target_bottom_left, target_top_right):
      return trajectrory
  # did not hit the target
  return None

def calc_height(trajectory):
  max_height = 0
  for pt in trajectory:
    max_height = max(max_height, pt[1])
  return max_height

def output(trajectory, target, max_height):
  y = max_height
  (tp0, tp1) = target
  print('')
  while y >= tp0[1]:
    line = ''
    x = 0
    while x <= tp1[0]:
      pt = (x,y)

      if pt == (0,0):
        line = line + 'S'
      elif pt in trajectory:
        line = line + '#'
      elif is_inside(pt, tp0, tp1):
        line = line + "T"
      else:
        line = line + "."
      x = x+1
    print(line)
    y = y-1

def get_similar_vels(start_vel):
  (dx,dy) = start_vel
  vels = []
  for x in range(-50,51):
    for y in range(-50,51):
      vel = (dx+x, dy+y)
      if vel != start_vel:
        vels.append(vel)
  return vels

def calc_possible_velocities(start_pt, target):
  (target_bottom_left, target_top_right) = (target[0], target[1])
  count = 0
  start_vel = (6,0)
  start_vel = (23, 98)
  vels_que = []
  used_vels = {}
  vels_que.append(start_vel)
  while len(vels_que) > 0:
    vel = vels_que.pop(0)
    used_vels[vel] = True
    trajectory = calc_trajectory((0,0), vel, target)
    if trajectory != None:
      count = count+1
      print(vel, count)
      similar_vels = get_similar_vels(vel)
      for similar_vel in similar_vels:
        if used_vels.get(similar_vel) == None:
          if not similar_vel in vels_que:
            vels_que.append(similar_vel)

  return count



start_pt = (0,0)
line = 'target area: x=20..30, y=-10..-5'
line = 'target area: x=265..287, y=-103..-58'
      #  'target area: x=265..287, y=-103..-58'
target = read_target(line)
result = calc_possible_velocities(start_pt, target)
print (result)

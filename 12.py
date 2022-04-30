# https://adventofcode.com/2021/day/12

import util



class Node:
  def __init__(self, name):
    self.name = name
    self.target_nodes = []

  def __repr__(self):
    target_names = ','.join([n.name for n in self.target_nodes])
    return f'{self.name}: {target_names}'

  def addTarget(self, node):
    for target_node in self.target_nodes:
      if target_node.name == node.name:
        raise Exception(f'Node already connected to {node.name}')
    self.target_nodes.append(node)

  def can_visit_once(self):
    return self.name == self.name.lower()

  def is_end(self):
    return self.name == 'end'


class Nodes:
  def __init__(self):
    # nodes are Node instances
    self.nodes = []

  def add(self, line):
    tok = line.split('-')
    name_a = tok[0]
    name_b = tok[1]
    node_a = self.get_or_create(name_a)
    node_b = self.get_or_create(name_b)
    node_a.addTarget(node_b)
    node_b.addTarget(node_a)


  def get_or_create(self, name):
    node = self.find(name)
    if node == None:
      node = Node(name)
      self.nodes.append(node)
    return node

  def find(self, name):
    for node in self.nodes:
      if node.name == name:
        return node
    return None



def visit(ways, node, way):
  if node.can_visit_once():
    if node in way:
      return
  way.append(node)
  if node.is_end():
    ways.append(way)
    return
  for target_node in node.target_nodes:
    visit(ways, target_node, way.copy())

def get_ways(nodes, ways):
  node_start = nodes.find('start')
  way = []
  visit(ways, node_start, way)


lines = util.read_data('./12.data')
nodes = Nodes()
for line in lines:
  nodes.add(line)


ways = []

get_ways(nodes, ways)


print(len(ways))


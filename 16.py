
# https://adventofcode.com/2021/day/16




def hex_to_bin(str):
  result = ''
  for w in str:
    integer = int(w, 16)
    binary = format(integer, '0>4b')
    result = result + binary
  return result


def read_bits(binary, n):
  s = binary[:n]
  return (binary[n:], s)

def read_value(binary):
  cont = True
  result = ''
  while cont:
    (binary, cont_bit) = read_bits(binary, 1)
    (binary, value_bits) = read_bits(binary, 4)
    result = result + value_bits
    cont = cont_bit == '1'
  return (binary, result)


def get_version_typeid_value(str):
  binary = hex_to_bin(str)
  (binary, version) = read_bits(binary, 3)
  version = int(version,2)
  (binary, typeid) = read_bits(binary, 3)
  typeid = int(typeid,2)
  (binary, value) = read_value(binary)
  value = int(value,2)
  return (version, typeid, value)



stream = 'D2FE28'
(version, typeid, value) = get_version_typeid_value(stream)
print(version, typeid, value)








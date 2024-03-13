# assumes no duplicates
def intersection(a, b):
  item_set = set(a)
  return [item for item in b if item in item_set]

# # more robust - accounts for duplicates
# def intersection(a, b):
#   return list(set(a).intersection(set(b)))

assert intersection([4,2,1,6], [3,6,9,2,10]) == [6, 2]
assert intersection([2,4,6], [4,2]) == [4, 2]
assert intersection([4,2,1], [1,2,4,6]) == [1, 2, 4]
assert intersection([0,1,2], [10,11]) == []

a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
assert intersection(a, b) == list(range(50000))
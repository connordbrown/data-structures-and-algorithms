def intersection(a, b):
  item_set = set(a)
  return [item for item in b if item in item_set]
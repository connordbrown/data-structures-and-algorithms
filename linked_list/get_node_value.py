class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    count += 1
    current = current.next
  return None

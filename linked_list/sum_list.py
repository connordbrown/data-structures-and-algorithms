class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
  sum = 0
  current = head
  while current is not None:
    sum += current.val
    current = current.next
  return sum
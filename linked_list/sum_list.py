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

# def sum_list(head):
#   if head is None:
#     return 0
#   return head.val + sum_list(head.next)

# test_01
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

assert sum_list(a) == 19

# test_02
x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

assert sum_list(x) == 42

# test_03
z = Node(100)

# 100

assert sum_list(z) == 100

# test_04
assert sum_list(None) == 0
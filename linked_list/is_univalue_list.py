class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True

# def is_univalue_list(head, prev_val = None):
#   if head is None:
#     return True
#   if prev_val is not None and head.val != prev_val:
#     return False
#   return is_univalue_list(head.next, head.val)

# test_01
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

# 7 -> 7 -> 7

assert is_univalue_list(a) == True

# test_02
a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4

assert is_univalue_list(a) == False

# test_03
u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

assert is_univalue_list(u) == True

# test_04
u = Node(2)
v = Node(2)
w = Node(3)
x = Node(3)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 3 -> 3 -> 2

assert is_univalue_list(u) == False

# test_05
z = Node('z')

# z

assert is_univalue_list(z) == True

# test_06
u = Node(2)
v = Node(1)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 1 -> 2 -> 2 -> 2

assert is_univalue_list(u) == False
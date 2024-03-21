class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

# def reverse_list(head, prev = None):
#   if head is None:
#     return prev
#   next = head.next
#   head.next = prev
#   return reverse_list(next, head)

# test_01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
# a -> b -> c -> d -> e -> f
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# f -> e -> d -> c -> b -> a
reverse_list(a) 

# test_02
x = Node("x")
y = Node("y")

# x -> y
x.next = y
# y -> x
reverse_list(x)

# test_03
p = Node("p")
# p
reverse_list(p) # p
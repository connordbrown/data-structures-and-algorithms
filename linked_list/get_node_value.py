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

# test_01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
assert get_node_value(a, 2) == 'c'

# test_02
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
assert get_node_value(a, 3) == 'd'

# test_03
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
assert get_node_value(a, 7) == None

# test_04
node1 = Node("banana")
node2 = Node("mango")
node1.next = node2

# banana -> mango
assert get_node_value(node1, 0) == 'banana'

# test_05
node1 = Node("banana")
node2 = Node("mango")
node1.next = node2

# banana -> mango
assert get_node_value(node1, 1) == 'mango'
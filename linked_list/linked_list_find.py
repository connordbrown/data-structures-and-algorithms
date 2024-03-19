class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

# def linked_list_find(head, target):
#   if head is None:
#     return False
#   if head.val == target:
#     return True
#   return linked_list_find(head.next, target)

# test_01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "c") # True

# test_02
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
linked_list_find(a, "d") # True

# test_03
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
linked_list_find(a, "q") # False

# test_04
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2
# jason -> leneli
linked_list_find(node1, "jason") # True

# test_05
node1 = Node(42)
# 42
linked_list_find(node1, 42) # True

# test_06
node1 = Node(42)
# 42
linked_list_find(node1, 100) # False

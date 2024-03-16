class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

# # helper function allows pass by reference of values list, preventing
# # copies from being creating and slowing down runtime
# def fill_values(head, values):
#     if head is None:
#         return
#     values.append(head.val)
#     fill_values(head.next, values)

# def linked_list_values(head):
#     values = []
#     fill_values(head, values)
#     return values

# test_01
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
assert linked_list_values(a) == ['a', 'b', 'c', 'd']

# test_02
x = Node("x")
y = Node("y")

x.next = y

# x -> y
assert linked_list_values(x) == ['x', 'y']

# test_3
q = Node("q")

# q
assert linked_list_values(q) == ['q']

# test_4
assert linked_list_values(None) == []
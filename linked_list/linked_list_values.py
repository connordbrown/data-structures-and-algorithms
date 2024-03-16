class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current)
        current = current.next
    return values

# helper function allows pass by reference of values list, preventing
# copies from being creating and slowing down runtime
def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)

def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values
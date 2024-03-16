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
# Write a function that returns whether a node is part of a cycle.
# HINT: Modify your DFS to return early when it finds a cycle

def part_of_a_cycle(a, j):
    """
    Given an adjacency list a and an index j, returns True if node j is part of a cycle, False if not.
    """
    # track visited nodes and nodes in current stack
    visited = set()
    stack = set()
    
    # visit all nodes in adjacency list - return True if cycle found else False
    for i in range(len(a)):
        if i not in visited:
            if dfs_helper(a, i, visited, stack, j):
                return True
    return False

def dfs_helper(graph, vertex, visited, stack, test_node):
    # add node to visited set
    visited.add(vertex)
    # add node to the stack
    stack.add(vertex)  
    
    # recursively traverse neighboring nodes
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            return dfs_helper(graph, neighbor, visited, stack, test_node)
        
        # cycle containing test_node detected 
        elif neighbor == test_node and neighbor in stack:
            return True
        
    # remove node from the stack after exploring its neighbors
    stack.remove(vertex)
    
    # no cycle detected
    return False


test_cases = [ 
    ([[1, 2, 3], [0, 2, 3], [0,1,3],[0,1,2]], 0, True),
    ([[1,3],[],[1,3],[2]], 0, False),
    ([[1,3],[],[1,3],[2]], 2, True),
    ([[],[0, 2],[3],[1]], 0, False),
    ([[],[0, 2],[3],[1]], 1, True),
    ([[1, 2], [4,5], [3,4], [8,9], [7,8], [6,7], [], [], [], []], 0, False)
]

for (test_graph, starting_node, solution) in test_cases:
    output = part_of_a_cycle(test_graph, starting_node)
    assert output == solution
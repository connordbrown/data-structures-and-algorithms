# Given an adjacency list a,  
# bfs(a, u) performs a breadth first search starting at node u and returns a list of nodes in the order in which they were seen.  
# INPUT: [[1], [2], [0]], 1  (a 3 node cycle, starting BFS at node 1)  
# OUTPUT: [1, 2, 0]
def bfs(a, u):
    from collections import deque
    # initialize queue with u as starting node
    queue = deque([u])
    # list of traversed nodes
    output = []
    # keep track of visited nodes - set has fast lookup
    visited = set()  

    # add nodes to output and remove them from queue
    # as they are visited
    while queue:
        current = queue[0]
        queue.popleft()
        if current not in visited:
            output.append(current)
            visited.add(current)
            for neighbor in a[current]:
                queue.append(neighbor)

    return output


test_cases = [ 
    ([[1, 2, 3], [0, 2, 3], [0,1,3],[0,1,2]], 0, [0,1,2,3]),
    ([[1,3],[0],[1,3],[2]], 0, [0, 1, 3, 2]),
    ([[],[0, 2],[3],[1]], 0, [0]),
    ([[],[0, 2],[3],[1]], 1, [1, 0, 2, 3]),
    ([[1, 2], [3,4], [5,6], [7,8], [8,9], [6,7], [], [], [], []], 0, [0,1,2,3,4,5,6,7,8,9])
]

for (test_graph, starting_node, solution) in test_cases:
    output = bfs(test_graph, starting_node)
    assert output == solution
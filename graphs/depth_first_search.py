# Given an adjacency list a,
# dfs(a) performs a depth first search starting at node 0 and returns a list of nodes in the order in which they were seen, with start and stop times.  
# INPUT: [[1], [2], [0]] (a 3 node cycle)  
# OUTPUT: [(0, (1, 6)), (1, (2, 5)), (2, (3, 4))]
    
def dfs(a):
    # keep track of visited nodes
    visited = set()
    # set time as global list variable - use list due to integers being immutable
    time = [0]
    
    # track nodes (keys) and their associated discovery/finish times (vals)
    traversal_times = {}
    
    # visit all nodes in adjacency list
    for i in range(len(a)):
        if i not in visited:
            dfs_visit(a, i, visited, traversal_times, time)
    
    # recover solution from traversal_times
    return get_solution(traversal_times)


def get_solution(traversal_times):
    # convert traversal_times dict into tuple list
    solution = []
    for node in traversal_times:
        solution.append((node, (traversal_times[node]['discovery'], traversal_times[node]['finish'])))
    return solution


def dfs_visit(graph, vertex, visited, traversal_times, time):
    # add node to visited set
    visited.add(vertex)
    
    # count recursive steps
    time[0] += 1
    
    # create dictionary for node if key nonexistent, record discovery time
    traversal_times[vertex] = traversal_times.get(vertex, {})
    traversal_times[vertex]['discovery'] = time[0]
    
    # recursively traverse neighboring nodes
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_visit(graph, neighbor, visited, traversal_times, time)
            
    # count return steps
    time[0] += 1
    # record finish time
    traversal_times[vertex]['finish'] = time[0]


test_cases = [ 
    ([[1, 2, 3], [0, 2, 3], [0,1,3],[0,1,2]], [(0, (1, 8)), (1, (2, 7)), (2, (3, 6)), (3, (4, 5))]),
    ([[1,3],[0],[1,3],[2]], [(0, (1, 8)), (1, (2, 3)), (3, (4, 7)), (2, (5, 6))]),
    ([[],[0, 2],[3],[1]], [(0, (1, 2)), (1, (3, 8)), (2, (4, 7)), (3, (5, 6))]),
    ([[],[0, 3],[1],[]],[(0, (1, 2)), (1, (3, 6)), (3, (4, 5)), (2, (7, 8))]),
    ([[1, 2], [4,5], [3,4], [8,9], [7,8], [6,7], [], [], [], []],[(0, (1, 20)), (1, (2, 13)), (4, (3, 8)), (7, (4, 5)), (8, (6, 7)), (5, (9, 12)), (6, (10, 11)), (2, (14, 19)), (3, (15, 18)), (9, (16, 17))])

]

for (test_graph, solution) in test_cases:
    output = dfs(test_graph)
    assert output == solution

# Input: An edge list with weights: [(0,1,1), (0,2,2),(1,2,1)]
# Output: A minimum spanning tree in the form of an edge list with weights: [(0, 1, 1), (1, 2, 1)]

# Note: Edge lists are lists of triples (i, j, w), with i < j, which represents an edge between nodes i and j with weight w. Edges are undirected in this assignment, and you should always return edges in the form (i, j, w), where i < j.
# Make sure to sort your final edge list in natural order, ie (0, 2, 1) before (1,2,1), (0,1,0) before (0,2,0).
# Hint: You can use heapq for the priority queue.

def convert_to_adjacency_list(edge_list):
    # create a set of vertices from edge_list
    vertices = {vertex for edge in edge_list for vertex in edge[0:2]}
    
    # create an adjacency list dictionary from vertices and edge_list
    graph_dict = {}
    for vertex in vertices:
        # create dictionary of neighbors
        graph_dict[vertex] = {}
        for edge in edge_list:
            if edge[0] == vertex:
                  graph_dict[vertex][edge[1]] = edge[2]
            if edge[1] == vertex:
                  graph_dict[vertex][edge[0]] = edge[2]
            
    return graph_dict

def get_solution(graph_dict):
    # convert graph_dict into a sorted list of tuples
    solution = []
    for node in graph_dict:
        for neighbor in graph_dict[node]:
            if node >= neighbor:
                solution.append((neighbor, node, graph_dict[node][neighbor]))
            else:
                solution.append((node, neighbor, graph_dict[node][neighbor]))
    solution.sort()
    return solution

def prim(a):
    import heapq
    starting_vertex = a[0][0]
    # convert a to graph dictionary
    graph = convert_to_adjacency_list(a)
    # initialize Minimal Spanning Tree (MST)
    mst = {} 

    visited = set([starting_vertex])
    # initialize edges queue list with starting vertex and its neighbors
    edges = [(weight, starting_vertex, ending_vertex) for ending_vertex, weight in graph[starting_vertex].items()]
    # convert edges to a heap priority queue
    heapq.heapify(edges)

    # while queue is not empty
    while edges:
        # extract minimum value from edge queue
        weight, frm, to = heapq.heappop(edges)
        # if neighboring node not in visited
        if to not in visited:
            # visit neighbor, add to visited and update MST with new edge
            visited.add(to)
            mst[frm] = mst.get(frm, {})
            mst[frm][to] = mst[frm].get(to, weight)
            # add next edge to queue
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))

    return get_solution(mst)


test_cases = [ 
    ([(0,1,1), (0,2,2),(1,2,1)], [(0, 1, 1), (1, 2, 1)]),
    ([(0,1,2), (0,4,1), (1,2,1), (1,4,2), (2,3,1), (3,4,1)], 
        [(0, 4, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)]),
    ([(0,1,1), (0,2,2), (0,3,1), (1,4,1), (1,5,2), (2,4,2), 
        (2,6,2), (3,5,2), (3,6,1), (4,7,2), (5,7,2), (6,7,1)], 
        [(0, 1, 1), (0, 2, 2), (0, 3, 1), (1, 4, 1), (1, 5, 2), (3, 6, 1), (6, 7, 1)]),
    ([(0,1,2), (0,2,2), (0,3,1), (1,4,1), (1,5,1), (2,4,2), 
        (2,6,1), (3,5,2), (3,6,2), (4,7,2), (5,7,2), (6,7,1)], 
        [(0, 1, 2), (0, 2, 2), (0, 3, 1), (1, 4, 1), (1, 5, 1), (2, 6, 1), (6, 7, 1)]) 
]

for (test_graph, solution) in test_cases:
    output = prim(test_graph)
    assert output == solution
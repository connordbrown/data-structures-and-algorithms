# Input: An edge list with weights: [(0,1,1), (0,2,2),(1,2,1)]
# Output: A minimum spanning tree in the form of an edge list with weights: [(0, 1, 1), (1, 2, 1)]

# Note: Edge lists are lists of triples (i, j, w), with i < j, which represents an edge between nodes i and j with weight w. Edges are undirected in this notebook, and you should always return edges in the form (i, j, w), where i < j. Make sure to sort your final edge list in natural order, ie (0, 2, 1) before (1,2,1), (0,1,0) before (0,2,0).
# Hint: Look into Python's Set class

def kruskal(a):
    # sort the mst in ascending order
    return sorted(kruskal_unsorted(a))

def kruskal_unsorted(a):
    # sort edge list in ascending order of weights
    a.sort(key=lambda edge: edge[2])
    
    # create a set of vertices from edge list a
    vertices = {vertex for edge in a for vertex in edge[0:2]}
    # create a disjoint-set dictionary with vertices as keys and sets of vertices as values
    sets = {vertex: {vertex} for vertex in vertices}
    # initialize Minimal Spanning Tree (MST)
    mst = []
    
    # for all edges in edge list
    for u, v, weight in a:
        # check if vertex u is in sets
        set_u = find_set(sets, u) 
        # check if vertex v is in sets
        set_v = find_set(sets, v) 
        # if not in the same set/forest
        if set_u != set_v: 
            # add sets[set_v] to forest (sets[sets_u])
            sets[set_u] = sets[set_u].union(sets[set_v])
            # remove the smaller set - already added to forest
            del sets[set_v]  
            # add edge to MST
            mst.append((u, v, weight))
    
    return mst

def find_set(sets, u):
    # check if u is contained in disjoint set
    for key, value in sets.items():
        if u in value:
            return key
    return None

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
    output = kruskal(test_graph)
    assert output == solution
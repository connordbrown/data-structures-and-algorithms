# You're given a list of bacteria RNA fragments, all from related bacteria which have mutated into separate strains over time. 
# Your goal is to come up with the most likely sequence of mutations that led to this state of affairs.

# The chance that one bacteria mutated into another depends on the number of differences in their RNA strings. The more differences
# in their RNA strings, the more unlikely it is that the bacteria mutated into each other.
# (In fact, exponentially more unlikely -- the probability that k locations changed at the same time is  2−𝑘 ).

# If we construct a fully connected graph whose nodes represent RNA fragments and each edge has weight 2−𝑘 , where k is the number of differences between RNA strings,
# then a spanning tree which maximizes the product of edge weights will be the most likely mutation tree.
# (Each mututation is assumed to be independent, so the chance that all the mutations in the spanning tree happen is the product of their respective probabilities)

# Write a function that takes a list of RNA fragments, constructs an edge list with weights, then returns the most likely mutation tree, along with its probability.

# Note: your algorithm should construct a graph and then run your implementation of Kruskal's algorithm on it. 
# The difficulty lies in determining the correct graph, so that a minimum sum spanning tree in your graph corresponds to a maximum product spanning tree in the graph described above.

# Input: ["adad","adac","acad", "cdac","addd"]
# Output: ([('adad', 'adac', 0.5), ('adad', 'acad', 0.5), ('adad', 'addd', 0.5), ('adac', 'cdac', 0.5)], 0.0625)

from kruskal import kruskal_unsorted

def mutation_tree(a):
    # construct an edge list with weights
    edge_list = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            # calculate the number of differences between RNA fragments
            k = sum(a != b for a, b in zip(a[i], a[j]))
            # calculate the weight of each edge
            weight = 2**(-k)
            edge_list.append((a[i], a[j], weight))
            
    # invert the weights - weights are < 1, so easy to do
    edge_list = [(u, v, 1 - weight) for u, v, weight in edge_list]
    # use vanilla Kruskal's MST algorithm to get MST with edges that maximize weight (inverted edge weights)
    mst = kruskal_unsorted(edge_list)
    # convert the MST back to original weights and calculate probability
    mst = [(u, v, 1 - weight) for u, v, weight in mst]
    
    probability = 1
    for _, _, weight in mst:
        probability *= weight
        
    return mst, probability


test_cases = [ 
    (["TAT", "CAT", "CAC"],([('TAT', 'CAT', 0.5), ('CAT', 'CAC', 0.5)], 0.25)),
    (["ACATA", "ATCTA", "GTCTA", "GTATA", "GCATA"], 
    ([('ACATA', 'GCATA', 0.5), ('ATCTA', 'GTCTA', 0.5), ('GTCTA', 'GTATA', 0.5), ('GTATA', 'GCATA', 0.5)], 0.0625)),
    (["GATTACA", "CGACTCA", "CATTACA", "CGACATA", "CGTTACA", "CGACACA", "CATTACG", "CGATACA"], 
        ([('GATTACA', 'CATTACA', 0.5), ('CGACTCA', 'CGACACA', 0.5), ('CATTACA', 'CGTTACA', 0.5), 
        ('CATTACA', 'CATTACG', 0.5), ('CGACATA', 'CGACACA', 0.5), ('CGTTACA', 'CGATACA', 0.5), ('CGACACA', 'CGATACA', 0.5)], 0.0078125)),
    (["CATTACA", "GATTACA", "CTTTACA", "CTGGTGA", "CTGTACA", "CTGGTCA", "CTGGTGC", "CTGGACA"], 
    ([('CATTACA', 'GATTACA', 0.5), ('CATTACA', 'CTTTACA', 0.5), ('CTTTACA', 'CTGTACA', 0.5), 
        ('CTGGTGA', 'CTGGTCA', 0.5), ('CTGGTGA', 'CTGGTGC', 0.5), ('CTGTACA', 'CTGGACA', 0.5), ('CTGGTCA', 'CTGGACA', 0.5)], 0.0078125))
]

for (test_graph, solution) in test_cases:
    output = mutation_tree(test_graph)
    assert output == solution

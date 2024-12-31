# We've provided a Tree class for you, which you can make a new Tree by calling,

# t1 = Tree(3) # t1 is a single node labeled 3 
# t2 = Tree(2, Tree(1), t1) # t2 is a Tree with root labeled 2 and two children labeled 1 and 3 
# t3 = Tree(1, None, Tree(2)) # t3 is a Tree with root labeled 1 and one right child labeled 2

# t1 = Tree(3)
# t2 = Tree(2, Tree(1), t1) # You can include Trees inside of Trees
# t3 = Tree(2, Tree(1), Tree(3))
# print(t3 == t2) # You can compare Trees using ==

class Tree:
    def __init__(self, value, leftTree = None, rightTree = None):
        self.value = value 
        self.leftSubtree = leftTree 
        self.rightSubtree = rightTree
    def __str__(self):
        return "Tree(" + str(self.value) + ", " + str(self.leftSubtree) + ", " + str(self.rightSubtree) + ")"
    def __eq__(self, otherTree):
        if self.value == otherTree.value and self.leftSubtree == otherTree.leftSubtree and self.rightSubtree == otherTree.rightSubtree:
            return True
        return False


# takes a preorder traversal of a binary tree (a list), and returns the Tree that it represents. Your algorithm should be recursive.
def preorderToTree(traversal):
    # base case: list is empty - traversal is complete
    if not traversal:
        return None
    
    # get root node - root is first element in preorder traversal
    root = traversal[0]
    
    # find index of first element greater than root - beginning of subtree to right of main root
    right_index = 1
    while right_index < len(traversal) and traversal[right_index] <= root:
        right_index += 1
    
    # recursively build left and right subtrees
    leftSubTree = preorderToTree(traversal[1:right_index])
    rightSubTree = preorderToTree(traversal[right_index:])
    
    # return tree object with root value and attached subtrees
    return Tree(root, leftSubTree, rightSubTree)


#  takes a preorder traversal of a BST (a list) and returns a postorder traversal of BST (another list), without using an intermediary Tree.
def preToPost(preTrav):
    # base case: preTrav list is empty - traversal is complete
    if not preTrav:
        return []
    
    # get root node - root is final element in postorder traversal
    root = preTrav[0]
    
    # find index of first element greater than root - beginning of subtree to right of main root
    right_index = 1
    while right_index < len(preTrav) and preTrav[right_index] <= root:
        right_index += 1
    
    # recursively build left and right sublists
    left_arr = preToPost(preTrav[1:right_index])
    right_arr = preToPost(preTrav[right_index:])
    
    # return composite list with root as final element
    return left_arr + right_arr + [root]


# preorderToTree tests
test_cases = [ 
    ([5, 2, 1, 3, 7, 6, 8], Tree(5, Tree(2, Tree(1), Tree(3)), Tree(7, Tree(6), Tree(8)))),
    ([5, 4, 3, 2, 1], Tree(5, Tree(4, Tree(3, Tree(2, Tree(1), None), None), None), None)),
    ([5, 6, 7, 8], Tree(5, None, Tree(6, None, Tree(7, None, Tree(8))))),
    ([5, 3, 4, 7, 6], Tree(5, Tree(3, None, Tree(4)), Tree(7, Tree(6), None)))
]

for (test_traversal, tree) in test_cases:
    output = preorderToTree(test_traversal)
    assert output == tree

# preToPost tests
test_cases = [ 
    ([5, 2, 1, 3, 7, 6, 8], [1, 3, 2, 6, 8, 7, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 6, 7, 8], [8, 7, 6, 5]),
    ([5, 3, 4, 7, 6], [4, 3, 6, 7, 5])
]

for (test_traversal, tree) in test_cases:
    output = preToPost(test_traversal)
    assert output == tree
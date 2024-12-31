# You must write the function preorderToTree, which takes a preorder traversal of a binary tree (a list), and returns the Tree that it represents. Your algorithm should be recursive.

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

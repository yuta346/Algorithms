class binaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
class binaryTree:
    def __init__(self):
        self.head = binaryTreeNode()

    def insertBst(self, num, tree):
        pass

    def insertNode(self, num, node):
        
        if node is None:
            new_node = binaryTreeNode()
            new_node.data = num
            node = new_node
            return node

        elif num < node.data:
            node.left = self.insertNode(num, node.left)

        elif num > node.data:
            node.right = self.insertNode(num, node.right)

        return node

bst = binaryTree()
bst.insertNode(5, )

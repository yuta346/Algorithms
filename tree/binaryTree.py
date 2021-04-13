class binaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
class binaryTree:
    def __init__(self,root):
        self.root = binaryTreeNode(root)

    def insertBst(self, num, head):
        tree.root = self.insertNode(num, head)

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

tree = binaryTree(1)

print(tree.root.data)

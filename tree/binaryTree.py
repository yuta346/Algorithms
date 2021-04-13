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
            new_node = binaryTreeNode(num)
            node = new_node
            return node

        elif num < node.data:
            node.left = self.insertNode(num, node.left)

        elif num > node.data:
            node.right = self.insertNode(num, node.right)
        return node

    def printTree(self, root): 
        if root is not None:
            self.printTree(root.left)
            print(root.data)
            self.printTree(root.right)
        

tree = binaryTree(5)
tree.insertBst(9,tree.root)
tree.insertBst(7,tree.root)
tree.insertBst(3,tree.root)
tree.insertBst(8,tree.root)
tree.insertBst(12,tree.root)

tree.printTree(tree.root)

# print(tree.root.data)
# print(tree.root.right.data)
# print(tree.root.right.right.data)

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
    
    def printPreOrder(self, root):
          if root is not None:
            print(root.data)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    def printPostOrder(self, root):
          if root is not None:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.data)
    

tree = binaryTree(10)
tree.insertBst(7,tree.root)
tree.insertBst(11,tree.root)
tree.insertBst(6,tree.root)
tree.insertBst(1,tree.root)
tree.insertBst(8,tree.root)
tree.insertBst(9,tree.root)
tree.insertBst(20,tree.root)
tree.insertBst(14,tree.root)
tree.insertBst(22,tree.root)
# tree.printPreOrder(tree.root)
tree.printPostOrder(tree.root)

# print(tree.root.data)
# print(tree.root.left.data)
# print(tree.root.left.left.data)
# print(tree.root.right.data)
# print(tree.root.right.right.data)

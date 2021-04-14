class binaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
class binaryTree:
    def __init__(self,root):
        self.root = binaryTreeNode(root)

    #returns true if root is empty and false otherwise
    def isEmpty(self, root):
        return root is None

    #Pre:tree is initialized
    #Post:call the recursive function insertNodes to insert the node in the tree and return the head node
    def insertBst(self, num, head):
        tree.root = self.insertNode(num, head)
        
    #Post:recursive function to insert the node in the tree
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
    
    #Post: perform pre-order traversal to print out the node in the tree
    def printPreOrder(self, root):
          if root is not None:
            print(root.data)
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    #Post: perform post-order traversal to print out the node in the tree
    def printPostOrder(self, root):
          if root is not None:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.data)
    
    #Post: perform in-order traversal to print out the node in the tree
    def printInOrder(self, root):
          if root is not None:
            self.printInOrder(root.left)
            print(root.data)
            self.printInOrder(root.right)

    #Pre:tree is initialized
    #Post:call the recursive function countNodes to count the number of nodes in the tree and return nuber of nodes
    def getLength(self, root):
        return self.countNodes(root)
    
    #Post: return the number of nodes in the tree
    def countNodes(self, root):
        if root is None:
            return 0
        else: 
            return self.countNodes(root.left)+self.countNodes(root.right)+1
    


    

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
# tree.printPostOrder(tree.root)
# tree.printInOrder(tree.root)
print(tree.getLength(tree.root))
print(tree.isEmpty(tree.root))

# print(tree.root.data)
# print(tree.root.left.data)
# print(tree.root.left.left.data)
# print(tree.root.right.data)
# print(tree.root.right.right.data)

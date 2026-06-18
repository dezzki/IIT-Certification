class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def Inorder(self,root): #left -> root -> right
        if root:
            self.Inorder(root.left)
            print(root.data, end=" ")
            self.Inorder(root.right)

    def Preorder(self,root): #root -> left -> right
        if root:
            print(root.data, end=" ")
            self.Preorder(root.left)
            self.Preorder(root.right)

    def Postorder(self,root): #left -> right -> root``
        if root:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.data, end=" ")

    def print_tree(self,root,level=0,prefix="Root: "):
        if root:
            self.print_tree(root.right,level+1, "R-------")
            print("         "*level+prefix+str(root.data),"\n")  #"     "*level= indentation + prefix + str.(root.data) = Cnncatination
            self.print_tree(root.left,level+1,"L-------")

root = Node(5)
root.left = Node(10)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(15)
root.right.left = Node(11)

# print(root.Inorder(root), "\n")
# print(root.Preorder(root), "\n")
# print(root.Postorder(root), "\n")
# 
# root.print_tree(root)



# Binary Search Tree
# - special kind of binary tree
# - each noded has at most 2 children(left and right)
# - left child contains values less than the node.
# - Right child contains values greater than node.

class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,root,data):
        if root is None:
            return BST(data)
        if data<root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)
        return root

    def search(self,root,target):
        if root is None:
            return False
        if root.data == target:
            return True
        elif root.data < target:
            return self.search(root.right,target)
        else:
            return self.search(root.left, target)
        
    def Inorder(self,root): #left -> root -> right
        if root:
            self.Inorder(root.left)
            print(root.data, end=" ")
            self.Inorder(root.right)

    def Preorder(self,root): #root -> left -> right
        if root:
            print(root.data, end=" ")
            self.Preorder(root.left)
            self.Preorder(root.right)

    def Postorder(self,root): #left -> right -> root``
        if root:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.data, end=" ")
        
    def delete(self,root,target):
        if root is None:
            return root
        
        if target<root.data:
            root.left=self.delete(root.left,target)
        elif target>root.data:
            root.right=self.delete(root.right,target)
        else: #Case 0 or Case 1
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

        #Case 2: Node has 2 children
        temp = self.find_min(root.right)

    def find_min(self,node):
        current = node
        while current.data

    def print_tree(self,root,level=0,prefix="Root: "):
        if root:
            self.print_tree(root.right,level+1, "R-------")
            print("         "*level+prefix+str(root.data),"\n")  #"     "*level= indentation + prefix + str.(root.data) = Cnncatination
            self.print_tree(root.left,level+1,"L-------")


bst = BST(10)
root = None
data = list(range(10,101,10))
for i in data:
    root = bst.insert(root,i)

bst.insert(root,55)


print(bst.print_tree(root))


print(bst.Inorder(root), "\n")
print(bst.search(root,4))



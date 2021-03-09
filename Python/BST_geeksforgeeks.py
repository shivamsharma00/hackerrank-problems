'''
Python Program of Binary Search Tree.

Code taken from : https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
python program to demonstrate 
insert operation in binary search tree
'''


# A utility class that represents
# an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# a utility function to insert a new 
# node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else: 
            root.left = insert(root.left, key)
    return root

# a utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def find_height(root):
    if root is None:
        return -1
    else:
        # compare the depth of each subtree
        l_depth = find_height(root.left)
        r_depth = find_height(root.right)

        # We will take biggest one
        if l_depth>r_depth:
            return l_depth+1
        else:
            return r_depth+1


'''
Driver program to test the above functions
Let us create the following BST

          50
        /    \
      30      70
     /  \    /  \
    20  40  60   80
'''   


if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # print inorder traversal of the BST
    # inorder(r)
    print(find_height(r))

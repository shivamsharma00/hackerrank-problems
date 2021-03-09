'''
This program contains code from Hackerrank.
It has Node class, and BST class which also claculate the height of BST.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None:
            return -1
        else:
            l_depth = self.getHeight(root.left)
            r_depth = self.getHeight(root.right)

            if l_depth > r_depth:
                return l_depth+1
            else:
                return r_depth+1

        #Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
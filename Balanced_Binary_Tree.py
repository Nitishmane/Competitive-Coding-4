# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self,root):
        if not root:
            return -1
        
        return max(self.height(root.left),self.height(root.right)) +1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        
    
    
        
       
        

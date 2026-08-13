# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are none, they are same
        if not p and not q:
            return True
        # if one of the nodes in None but other is not, thats False
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        left, right = self.isSameTree(p.right, q.right), self.isSameTree(p.left, q.left)
        return left and right

        
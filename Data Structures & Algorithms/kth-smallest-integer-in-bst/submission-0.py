# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        processed = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            processed.append(node.val)
            dfs(node.right)
        # this function noes really return anything
        dfs(root)
        return processed[k-1]
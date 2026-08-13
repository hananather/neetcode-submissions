# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        m = root.val
        good_nodes = 0
        def dfs(node, m):
            if not node:
                return 0
            if node.val >= m:
                nonlocal good_nodes 
                good_nodes =  good_nodes + 1 # good node
                m = node.val
            left = dfs(node.left, m)
            right = dfs(node.right, m)
        dfs(root, m)
        return good_nodes


        
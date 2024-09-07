# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def get_sum(root):
            total = 0
            if root.left:
                if not root.left.left and not root.left.right:
                    total += root.left.val
            
            if root.left:
                total += get_sum(root.left)
            if root.right:
                total += get_sum(root.right)
            return total

        return get_sum(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = {}
        def validate_tree(_root):
            complement = k - _root.val
            if complement in hashmap:
                return True
            hashmap[_root.val] = True
            if _root.left:
                value = validate_tree(_root.left)
                if value: return value
            if _root.right: 
                value = validate_tree(_root.right)
                if value: return value
        if root: return validate_tree(root)
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1
        queue = [root]
        while queue:
            # Iterate through the current level
            for _ in range(len(queue)):
                temp = queue.pop(0)
                
                # If it's a leaf node, return the current depth level
                if not temp.left and not temp.right:
                    return level
                
                # Add children to the queue
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            
            # Increment depth level after finishing processing all nodes of the current level
            level += 1
        
        return level
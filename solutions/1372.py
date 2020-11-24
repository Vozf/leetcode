# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # true - left, false - right
        result = 0
        stack = [(root, True, 0, 0), (root, False, 0, 0)]
        while len(stack) > 0:
            node, direction, depth, real_depth = stack.pop()
            if depth > result:
                result = depth
            child = node.left if direction else node.right
            reset_child = node.left if not direction else node.right 
            if reset_child is not None:
                stack.append((reset_child, direction, 1, real_depth+1))
            if child is not None:
                stack.append((child, not direction, depth+1, real_depth+1))
        return result

        

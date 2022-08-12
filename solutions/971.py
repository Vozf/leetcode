# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myrec(self, root, voyage):
        arr = []

        if root is None:
            return [], voyage
        
        if root.val != voyage[0]:
            return [-1], voyage
            
        
        left_list, new_voyage = self.myrec(root.left, voyage[1:])
        right_list, new_voyage = self.myrec(root.right, new_voyage)
        if (len(left_list) == 1 and left_list[0] == -1) or (len(right_list) == 1 and right_list[0] == -1):
            left_list, new_voyage = self.myrec(root.right, voyage[1:])
            right_list, new_voyage = self.myrec(root.left, new_voyage)
            
            if (len(left_list) == 1 and left_list[0] == -1) or (len(right_list) == 1 and right_list[0] == -1):
                return [-1], voyage
            else:
                return left_list + right_list + [root.val], new_voyage

        else:
            return left_list + right_list, new_voyage
        
        
            
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        return self.myrec(root, voyage)[0]

             
            
            
            

        

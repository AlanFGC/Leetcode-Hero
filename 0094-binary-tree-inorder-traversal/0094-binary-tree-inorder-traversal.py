# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        node = root
        def traverse(node, res):
            if not node:
                return
            
            if node.left:
                traverse(node.left, res)
            
            res.append(node.val)
            
            if node.right:
                traverse(node.right, res)
        
        traverse(node, res)
        
        return res
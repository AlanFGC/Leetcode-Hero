# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris implementation of traversal
        """
        res = []
        node = root
        "algo ends when current is null"
        while node:
            # no left child
            if not node.left:
                res.append(node.val)
                node = node.right
                continue
            
            # main algo
            
            pred = self.findPredecessor(node)
            print(f'{pred.val}')
            
            # if predecessor exists we connect it to the top node
            # we will do this till he have added all the LEFT nodes in this
            # branch
            if not pred.right:
                pred.right = node
                node = node.left
            else:
                pred.right = None
                res.append(node.val)
                node = node.right
        
        return res
                
                
                
    
    def findPredecessor(self, node: TreeNode)-> TreeNode:
        curr = node
        node = node.left
        while node.right is not None and node.right != curr:
            node = node.right
            
        return node
            
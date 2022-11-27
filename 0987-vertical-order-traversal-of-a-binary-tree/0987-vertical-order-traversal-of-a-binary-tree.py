# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class newTree(TreeNode):
    def __init__(self, val=0, left=None, right=None, vert=0, lvl=0):
        super().__init__(val, left, right)
        self.vert = vert
        self.lvl = lvl
        
def convertOldRoot(old:TreeNode, vert:int, lvl:int) -> newTree:
    return newTree(old.val, old.left, old.right, vert, lvl)
    


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # in order traversal
        node = root
        
        def traverseNode(node, vert, lvl):
            if not node:
                return None
            
            # do some operation here
            newNode = convertOldRoot(node, vert, lvl)
            
            newNode.left = traverseNode(node.left, vert - 1, lvl+1)
            newNode.right = traverseNode(node.right, vert + 1, lvl+1)
            
            return newNode
        
        
        newRoot = traverseNode(root, 0, 0)
        
        myMap = {}
        
        
        
        
        def normalTraversal(node: newTree, myMap):
            if not node:
                return None
            
            # do some operation here
            if node.vert in myMap:
                myMap[node.vert].append(node)
            else:
                myMap[node.vert] = [node]
            
            node.left = normalTraversal(node.left, myMap)
            node.right = normalTraversal(node.right, myMap)
            
            return node
        
        normalTraversal(newRoot, myMap)
        
        keyList = list(myMap.keys())
        keyList.sort()

        
        res = []
        for i in range(len(keyList)):
            res.append(myMap[keyList[i]])
        
        
        for item in res:
            item.sort(key=lambda item: (item.lvl, item.val))
            
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = res[i][j].val
        
            
        return res
        
        
        
            

        
            
            
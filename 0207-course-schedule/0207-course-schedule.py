class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topological sort uses dfs to traverse all the nodes and in reverse order findout which
        course goes first.
        In this problem dependencies are an issue and if we find a dependency loop, 
        we return False
        """
        
        
        # all my courses with their dependencies
        courses = {}
        
        for i in range(len(prerequisites)):
            item = prerequisites[i]
            print(item)
            if item[0] not in courses:
                courses[item[0]] = set()
                courses[item[0]].add(item[1])
            else:
                courses[item[0]].add(item[1])
            if item[1] not in courses:
                courses[item[1]] = set()
                
      
        # just as Ford fulkerson we disconnect the traverse function (DFS or BFS)
        for item in courses.items():
            recStack = [False] * numCourses # this stack functions the stack we use, if we see that we visited a node twice, we check in stack
            # if true, it's a cycle, the stack tells have we visited on the dfs run.
            visited = set() 
            
            # visited set server more like a dp, where we already know the answer, if new and true
            if self.dfs(item[0], courses, visited, recStack): return False
            
        return True
    
    
    # we have to check that current course can be completed
    # by checking all the courses before it.
    def dfs(self, current, nodes, visited, recStack): 
        # mark the current Stack as visited
        recStack[current] = True
        visited.add(current)
        
        
 
        
        for item in nodes[current]:
            
            if current in nodes[item]:
                return True
            
            #if the item hast not been visited, visit and check for the same things
            if item not in visited:
                # check the nodes if one finds cycle you are also done
                if self.dfs(item, nodes, visited, recStack):
                    return True
            # if the item has been visited and it's in the current stack, that means that there is a cycle!!
            elif recStack[item] is True:
                return True
            
        # if no cycles found we can set it to false again
        recStack[current] = False
        return False
        
        
        
        
        
        
        
        
        

        
        
        
            
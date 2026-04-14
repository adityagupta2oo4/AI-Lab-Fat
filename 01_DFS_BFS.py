
#defining the graph

tree  = {
    'S' : ['A','B','C'],
    'A' : ['D','E'], 'B' : ['F','G'],
    'D' : ['K','L'] , 'E' : ['M'],
}

# defining goal nodes

goals = { 'G','I','L','X','P'}

# depth first search function

def dfs(start) :
    
    visited = []
    found_goal = None
    
    #main part is here 
    
    def recurse(node):
        
        nonlocal found_goal # in order to store the value in outer found_goal
                            # so that it doesn't end recursion
        if found_goal: return # stop recursion once found gaol saare brach ko end yhi karega  
        
        #if not 
        visited.append(node)
        
        if node in goals:
            found_goal = node 
            return   # if current node is goal node then assign found_goal then end the current branch 
        
        # here comes the recurcion part
        
        for child in  tree.get(node, []): # if no child then give []
            recurse(child)
        
    
    recurse(start) # recusrion ka starting point
    return visited,found_goal
    

#Breadth First Search

def bfs(start):
    
    visited = []
    found_goal = None
    
    queue = [start] # queue me start node daal do
    
    while queue:
        node = queue.pop(0) # queue se first element nikal lo
        
        if node not in visited: # agar visited me nahi hai to visit karo
            visited.append(node)
            
            if node in goals: # agar current node goal hai to assign karo found_goal me
                found_goal = node
                break # stop the loop once found goal
            
            # add children to the queue
            queue.extend(tree.get(node, [])) # agar no child then give []
    
    return visited,found_goal
    
start = 'S'

order,first_goal = bfs(start);

print(order)
print(first_goal)

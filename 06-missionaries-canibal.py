
#missionaries and cannibal

from collections import deque # we are going to use bfs

def is_valid(m,c):
    
    if m<0 or c<0 or m>3 or c> 3: return False
    
    if m> 0 and m<c : return False # check on the left side
    
    if (3-m)>0 and (3-m)<(3-c): return False # check on the right side
    
    return True
    
def solve_missionaries():
    
    start = (3,3,1) # initial state
    goal = (0,0,0) # final state
    
    queue = deque([(start , [start])]) # state,path important syntax
    
    visited = {start} # visited node
    
    # possible boat moves
    
    moves = [(1,0),(0,1),(2,0),(0,2),(1,1)]
    while queue:
        
        (m,c,b),path =  queue.popleft()
        
        if (m,c,b) ==  goal: return path
        
        for dm,dc in moves:
            
            if b == 1 : # boat is on the left side
                new_state = (m-dm,c-dc,0)
            else :
                new_state = (m+dm,c+dc,1)
                
            nm,nc,nb = new_state
            
            if is_valid(nm,nc) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    return None
    

      # ---- Run and Display ---
solution = solve_missionaries()
if solution:
    print(f'Solution in {len(solution)-1} steps:')
    for step, (m, c, b) in enumerate(solution):
        side = 'Left' if b else 'Right'
        print(f'  Step {step}: Left=({m}M,{c}C) Right=({3-m}M,{3-c}C) Boat={side}')
else:
    print('No solution found.')      
        
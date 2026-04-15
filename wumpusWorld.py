
#wumpus world problem
                    
#Defining our constants

SIZE  = 4
AGENT = 'A'
PIT = 'P'
WUMPUS = 'W'
GOLD = 'G'
BREEZE  = 'B'
STENCH = 'S'
EMPTY = '.'

#definng position 

agent = (1,1)
wumpus = (1,3)
pit  = (3,3)
gold = (4,4)
    
#following 1-n position convetion

#creating grid

grid = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

#function to find neighbours

def neighbors(x,y):
    #possible movement
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    
    result = []
    
    for dr,dc in direction:
        nr = x + dr
        nc = y + dc
        
        if 1<=nr<=SIZE and 1<=nc<=SIZE:
            result.append((nr,nc))
    
    return result

# function to place symbol

def place(symbol , pos):
    r,c = pos
    grid[r-1][c-1] = symbol # since followong 1- n 
    
# placing all the symbol

place(AGENT,agent)
place(PIT,pit)
place(WUMPUS,wumpus)
place(GOLD,gold)


#adding breeaze around pit

for n in neighbors(*pit):
    r,c = n
    
    if grid[r-1][c-1] == EMPTY:
        grid[r-1][c-1]  = BREEZE

# adding the stench

for n in neighbors(*wumpus):
    r,c = n
    
    if grid[r-1][c-1] == EMPTY:
        grid[r-1][c-1] = STENCH
    elif grid[r-1][c-1] == BREEZE:
        grid[r-1][c-1] = 'B'

# to print the grid

def print_grid():
    
    print("   1 2 3 4")
    for r in range(SIZE,):
        print(r+1,"|",end = "")
        
        for c in range(SIZE):
            print(grid[r][c] , end = " ")
        print("\n")

    
print("\nInitial setup")

print_grid()

#movement simulation with grid

def simulate(path):
    global agent
    
    
    for step in path:
        # removing from old cell
        r, c = agent
        grid[r-1][c-1] = EMPTY
        
        #move agent 
        
        agent = step
        r, c = agent
        cell = grid[r-1][c-1] 
        
        print("agent move to step: ",step)
        
        if cell == PIT:
            grid[r-1][c-1] = AGENT
            print_grid()
            print("Agent fell in to pit")
            return
        elif cell == STENCH:
            grid[r-1][c-1] = AGENT
            print_grid()
            print("Agent sense stench")
        elif cell == BREEZE:
            grid[r-1][c-1] = AGENT
            print_grid()
            print("Agent sense breeze")
        elif cell ==WUMPUS:
            grid[r-1][c-1] = AGENT
            print_grid()
            print("eaten by wumpus")
            return
        elif cell == GOLD:
            grid[r-1][c-1] = AGENT
            print_grid()
            print("found gold")
            return
        
        # it's empty
        grid[r-1][c-1] = AGENT
        print_grid()
        
        
death_path = [(1,1),(1,2),(1,3)]
simulate(death_path)

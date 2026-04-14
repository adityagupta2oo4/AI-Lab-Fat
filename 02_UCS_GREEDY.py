#UCS and Greedy

import heapq

'''
 from heapq hum do specif method use krne wale hai 
    m-1 : heapq.heappop("here your list") - pop node with least cummaltive cose
    m- 2 : heapq.heappush(list,element) - push in heap 

'''

# Weighted undirected graph: node -> list of (neighbor, cost)
graph = {
    'a': [('b', 32), ('f', 3)],
    'b': [('a', 32), ('f', 7), ('c', 21), ('e', 12)],
    'f': [('a', 3), ('b', 7), ('c', 2)],
    'c': [('f', 2), ('b', 21), ('e', 6), ('g', 11)],
    'e': [('b', 12), ('c', 6), ('d', 13)],
    'd': [('e', 13), ('g', 9)],
    'g': [('d', 9), ('c', 11)],
}
# UCS - > expand the node jiska commulative cost sbse km ho

def uniform_cost_search(graph,start,goal):
    
    pq = [(0,start,[])] #priority queue: (cost,node , path)
    
    visited = set() 
    
    while pq:
        cost , node , path = heapq.heappop(pq)
        
        # is the alredy visited if yes move to next iteration
        
        if node in visited : continue
        
        # not visited 
        visited.add(node)
        path = path + [node] #extending the new node
        
        if node == goal : return path,cost # gaol pe pahoch gye to return cost aur path
        
        # ab us node ke sare explored node ko add kardo
        
        for neighbour , edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq,(cost+edge_cost,neighbour,path))
                
a, b = uniform_cost_search(graph,'a','g')

print(a)
print(b)
                
                

#greeady BFS
#everything is same as UCS just here we use heuristic

heuristic = { 'a' : 10 , 'b' : 6, 'c' : 2 , 'd' : 1 , 'e' : 5 , 'f':8 , 'g':0}

def greedy_bfs(graph , start , goal):
    
    pq = [(heuristic[start],start , [])]
    visited = set()
    
    while pq:
        _ , node , path = heapq.heappop(pq) # _ beacuse we are not using the cost factor here
        
        if node in visited : continue
        
        visited.add(node)
        path = path + [node]
        
        if node  == goal :
            return path
        
        for neighbor , _ in graph[node]: # _ beacuse we are not using the cost factor here
            if neighbor not in visited: 
                heapq.heappush(pq,(heuristic[neighbor],neighbor,path))
        
        
print(greedy_bfs(graph , 'a','g'))


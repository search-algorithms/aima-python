def iterative_dfs(graph,start,path=[]):
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path = path+[v]
            q = graph[v] + q
    return path    

def recursive_dfs(graph,start,path=[]):
    path=path+[start]
    for node in graph[start]:
        if node not in path:
            path=recursive_dfs(graph,node,path)
    return path

    
def iterative_bfs(graph,start,path=[]):
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path = path+[v]
# put on end of queue
            q = q + graph[v] 
    return path    

    
"""
A
| \
B  C
|
D
bfs: ABCD
dfs: ABDC
"""

graph={
    'A':['B','C'],
    'B':['D'],
    'C':[],
    'D':[]
}

print 'recursive dfs',recursive_dfs(graph,'A')
print 'dfs',iterative_dfs(graph,'A')
print 'bfs',iterative_bfs(graph,'A')



map1 = {
'S': ['A','B'],
'A': ['B'],
'B': ['C'],
'C': ['G'],
}

def simple_dfs(start,goal,neighbors):
    stack=[(start,)]
    while stack:
        print('dfs:stack',stack)
        path=stack.pop()
        s=path[-1]
        print('dfs:popping',path)
        #print('dfs:visit',s)
        if s == goal:
            return path
        else:
            # put new path extensions on front of queue/stack
            # stack = [('s','a'), ('s','b')]
            for s2 in neighbors[s]:
                # extension of path
                path2 = path + (s2,)
                print('dfs:extending path', path2)
                stack=stack+[path2]
        
def simple_bfs(start,goal,neighbors):
    stack=[(start,)]
    while stack:
        print('bfs:stack',stack)
        path=stack.pop(0)
        print('bfs:popping',path)
        s=path[-1]
        #print('bfs:visit',s)
        if s == goal:
            return path
        else:
            # put new path extensions on back of queue/stack
            # stack = [('s','a'), ('s','b')]
            for s2 in neighbors[s]:
                # extension of path
                path2 = path + (s2,)
                print('bfs:extending path', path2)
                stack=stack+[path2]
        
"""
S
| \
A  B
   |
   C
   |
   G
bfs: S,B,C,G
dfs: S,B,C,G

A
| \
B  C
|  | \
D  E  F

dfs
(A)
(AB)(AC)
(ABD),(AC)
(AC)
(ACE),(ACF)

bfs
(A)
(AB),(AC)
(ABD),(AC)
(ABD),(ACE),(ACF)

simple_dfs
('dfs:stack', [('A',)])
('dfs:popping', ('A',))
('dfs:extending path', ('A', 'B'))
('dfs:extending path', ('A', 'C'))
('dfs:stack', [('A', 'B'), ('A', 'C')])
('dfs:popping', ('A', 'C'))
('dfs:extending path', ('A', 'C', 'E'))
('dfs:extending path', ('A', 'C', 'F'))
('dfs:stack', [('A', 'B'), ('A', 'C', 'E'), ('A', 'C', 'F')])
('dfs:popping', ('A', 'C', 'F'))
('A', 'C', 'F')
simple_bfs
('bfs:stack', [('A',)])
('bfs:popping', ('A',))
('bfs:extending path', ('A', 'B'))
('bfs:extending path', ('A', 'C'))
('bfs:stack', [('A', 'B'), ('A', 'C')])
('bfs:popping', ('A', 'B'))
('bfs:extending path', ('A', 'B', 'D'))
('bfs:stack', [('A', 'C'), ('A', 'B', 'D')])
('bfs:popping', ('A', 'C'))
('bfs:extending path', ('A', 'C', 'E'))
('bfs:extending path', ('A', 'C', 'F'))
('bfs:stack', [('A', 'B', 'D'), ('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:popping', ('A', 'B', 'D'))
('bfs:stack', [('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:popping', ('A', 'C', 'E'))
('bfs:stack', [('A', 'C', 'F')])
('bfs:popping', ('A', 'C', 'F'))
('A', 'C', 'F')

simple_dfs
('dfs:stack', [('A',)])
('dfs:visit', 'A')
('dfs:stack', [('A', 'B'), ('A', 'C')])
('dfs:visit', 'C')
('dfs:stack', [('A', 'B'), ('A', 'C', 'E'), ('A', 'C', 'F')])
('dfs:visit', 'F')
('A', 'C', 'F')
simple_bfs
('bfs:stack', [('A',)])
('bfs:stack', [('A', 'B'), ('A', 'C')])
('bfs:stack', [('A', 'C'), ('A', 'B', 'D')])
('bfs:stack', [('A', 'B', 'D'), ('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:stack', [('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:stack', [('A', 'C', 'F')])
('A', 'C', 'F')

simple_dfs
('dfs:stack', [('A',)])
('dfs:visit', 'A')
('dfs:stack', [('A', 'C'), ('A', 'B')])
('dfs:visit', 'B')
('dfs:stack', [('A', 'B', 'D'), ('A', 'C')])
('dfs:visit', 'C')
('dfs:stack', [('A', 'C', 'F'), ('A', 'C', 'E'), ('A', 'B', 'D')])
('dfs:visit', 'D')
('dfs:stack', [('A', 'C', 'F'), ('A', 'C', 'E')])
('dfs:visit', 'E')
('dfs:stack', [('A', 'C', 'F')])
('dfs:visit', 'F')
('A', 'C', 'F')
simple_bfs
('bfs:stack', [('A',)])
('bfs:stack', [('A', 'B'), ('A', 'C')])
('bfs:stack', [('A', 'C'), ('A', 'B', 'D')])
('bfs:stack', [('A', 'B', 'D'), ('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:stack', [('A', 'C', 'E'), ('A', 'C', 'F')])
('bfs:stack', [('A', 'C', 'F')])
('A', 'C', 'F')

"""
simple1= {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['E','F'],
    'D': [],
    'E': [],
    'F': [],
}


print('simple_dfs')
print(simple_dfs('A','F',simple1))
print('simple_bfs')
print(simple_bfs('A','F',simple1))

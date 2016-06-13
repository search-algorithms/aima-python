import sys
from collections import deque # Doubly-ended queue: pop from left, append to right.

def simple_bfs(start,goal,neighbors):
    stack=[(start,)]
    extensions=1
    while stack:
        path=stack.pop()
        s=path[-1]
        print('PATH',path)
        print('SSSS',s)
        if s==goal:
            print('extensions',extensions)
            return path
        else:
            for s2 in neighbors[s]:
                print('SSS2',s2)
                path2 = path + (s2,)
                print ('PATH2', path2)
                extensions+=1
# add to end of queue for BFS
                stack = stack + [path2]
                print('STACK',stack)

def simple_dfs(start,goal,neighbors):
    stack=[(start,)]
    extensions=1
    while stack:
        path=stack.pop()
        s=path[-1]
        print('PATH',path)
        print('SSSS',s)
        if s==goal:
            print('extensions',extensions)
            return path
        else:
            for s2 in neighbors[s]:
                print('SSS2',s2)
                path2 = path + (s2,)
                print ('PATH2', path2)
                extensions+=1
                stack = [path2] + stack

def breadth_first(start, goal, neighbors):
    "Find a shortest sequence of states from start to the goal."
    frontier = deque([start]) # A queue of states
    previous = {start: None}  # start has no previous state; other states will
    while frontier:
        s = frontier.popleft()
        if s == goal:
            return path(previous, s)
        for s2 in neighbors[s]:
            if s2 not in previous:
                frontier.append(s2)
                previous[s2] = s
                
def path(previous, s): 
    "Return a list of states that lead to state s, according to the previous dict."
    return [] if (s is None) else path(previous, previous[s]) + [s]

def depth_first(start, goal, neighbors):
    "Find a shortest sequence of states from start to the goal."
    frontier = deque([start]) # A queue of states
    previous = {start: None}  # start has no previous state; other states will
    while frontier:
        print('Frontier',frontier)
        s = frontier.pop()
        print('DEPTH: popping %s' % s)
        if s == goal:
            return path(previous, s)
        for s2 in neighbors[s]:
            if s2 not in previous:
                frontier.appendleft(s2)
                previous[s2] = s
                print('appending',s2,'PREVIOUS',previous)


romania = {
 'A': ['S', 'T','Z'],
 'B': ['F', 'G','P', 'U'],
 'C': ['D', 'P', 'R'],
 'D': ['C','M'],
 'E': ['H'],
 'F': ['B','S'],
 'G': ['B'],
 'H': ['E','U'],
 'I': ['N', 'V'],
 'L': ['M','T'],
 'M': ['D','L'],
 'N': ['I'],
 'O': ['S','Z'],
 'P': ['B','C','R'],
 'R': ['C','P','S'],
 'S': ['A','F', 'O', 'R'],
 'T': ['A', 'L'],
 'U': ['B', 'H', 'V'],
 'V': ['I','U'],
 'Z': ['A','O']}

print ('breadth_first',breadth_first('A', 'B', romania))  #  A,S,F,B
# print ('simple_bfs',simple_bfs('A', 'B', romania)) 
# sys.exit(1)
print ('depth_first',depth_first('A', 'B', romania)) 
print ('simple_dfs',simple_dfs('A', 'B', romania)) 
"""
#(A)
(A,S),(A,T),(A,Z)
depth: A,S,F,B
depth first search path from A to Z: 
(A)
(A,S),(A,T),(A,Z)
(A,S,F),(A,S,O),(A,S,R),(A,T),(A,Z)
(A,S,F,B),(A,S,O),(A,S,R),(A,T),(A,Z)

"""
print ('>>>>>>>>>>>>>>>depth_first A to Z: ')
print ('>>>>>>>>>>>>>>>END depth_first A to Z: ',depth_first('A', 'Z', romania)) 
print ('>>>>>>>>>>>>>>>depth_first A to ZZ: ')
print ('>>>>>>>>>>>>>>>END depth_first A to ZZ: ',depth_first('A', 'ZZ', romania)) 
OLD_mit_patrick_winston = {
    'S': ['AA','B'],
    'AA': ['B','D','S'],
    'B': ['AA','C','S'],
    'C': ['AA','E'],
    'D': ['AA','G'],
    'E': ['C'],
    'G': ['D'],
}

mit_patrick_winston = {
    'S': ['AA','B'],
    'AA': ['B','D'],
    'B': ['C'],
    'C': ['E'],
    'D': ['G'],
    'E':[],
    #'
    #'E': ['C'],
    #'G': ['D'],
}
# S,A,D,G
print ('depth_first',depth_first('S', 'G', mit_patrick_winston)) 
# S,A,B,C,E,D,G


            


print ('simple_dfs',simple_dfs('S', 'G', mit_patrick_winston)) 

print ('breadth_first',breadth_first('S', 'G', mit_patrick_winston)) 


print ('simple_bfs',simple_bfs('S', 'G', mit_patrick_winston)) 

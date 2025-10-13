from collections import deque
import json

G = {
    'A': ['C', 'B'],
    'B': ['C'],
    'C': ['D', 'B', 'A'],
    'D': ['C']
}

def getPpaths(G, r):
    p, Q = { r: None }, deque([r])

    while Q:
        node = Q.popleft()
        
        for n in G[node]:
            if n not in p and n not in Q:
                p[n] = node
                Q.append(n)
    
    return p

p = getPpaths(G, 'A')

print(json.dumps(p, indent=4))

def getShortestPath(G, r, s):
    p = getPpaths(G, r)

    if s not in p: 
        return []
    
    pred = p[s]
    path = [s]
    while pred:
        path.append(pred)
        pred = p[pred]

    path.reverse()

    return path
    
print("path from A to D:", getShortestPath(G, 'A', 'D'))
print("path from B to D:", getShortestPath(G, 'B', 'D'))
print("path from D to B:", getShortestPath(G, 'D', 'B'))

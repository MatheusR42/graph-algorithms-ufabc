import json

D = {
    1: [2, 4],
    2: [3, 5],
    3: [6],
    4: [3, 6],
    5: [7],
    6: [5],
    7: [6]
}

def getPpaths(D, r):
    p = { r: None }
    visited = set()
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        for next in D[node]:
            if next not in p:
                p[next] = node
                dfs(next)
    
    dfs(r)
    return p

p = getPpaths(D, 1)
print(json.dumps(p, indent=4))

def getPath(D, r, s):
    p = getPpaths(D, r)
    
    if s not in p:
        return []
    
    pred = p[s]
    path = [s]
    while pred:
        path.append(pred)
        pred = p[pred]
    
    path.reverse()
    return path

print("path from 1 to 6:", getPath(D, 1, 6))
print("path from 1 to 7:", getPath(D, 1, 7))
print("path from 2 to 6:", getPath(D, 2, 6))

    
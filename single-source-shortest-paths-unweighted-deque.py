from collections import deque

def mlp(G, r):
    p, F = {r: None}, deque([r])

    while F:
        current_node = F.popleft()
        for neighbor in G[current_node]:
            if neighbor not in p:
                F.append(neighbor)
                p[neighbor] = current_node
    return p

G = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

r = 'A'

shortest_path_tree = mlp(G, r)

print(f"Shortest path tree from source vertex '{r}':")
import json
print(json.dumps(shortest_path_tree, indent=4))


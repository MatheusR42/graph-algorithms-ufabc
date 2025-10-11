def mlp(G, r):
    p, F = {r: None}, [r]
    while F:
        Fl = []
        for current_node in F:
            for neighbor in G[current_node]:
                if neighbor not in p:
                    Fl.append(neighbor)
                    p[neighbor] = current_node
        F = Fl
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


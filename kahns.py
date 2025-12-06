from collections import deque

D = {
    1: [3, 4],
    2: [3, 5],
    3: [6],
    4: [6, 7],
    5: [7],
    6: [8],
    7: [8],
    8: []  # N+(8) is empty set
}

def findTopologicalOrdering(D):
    Q = deque([])
    order = []
    in_degree = {}

    # Initialize in_degree for all vertices (both keys and values)
    for v in D.keys():
        in_degree[v] = 0
    for v in D.keys():
        for to in D[v]:
            if to not in in_degree:
                in_degree[to] = 0

    # setting degree of each vertice
    for v in D.keys():
        for to in D[v]:
            in_degree[to] += 1

    # adding vertices without dependencies to the queue
    for v in D.keys():
        if in_degree[v] == 0:
            Q.append(v)
    
    # sorting the queue. This is not necessary. We only do this to be easy to understand
    Q = deque(sorted(Q))

    while Q:
        at = Q.popleft()
        order.append(at)

        for to in D[at]:
            in_degree[to] -= 1
            if in_degree[to] == 0:
                Q.append(to)
        
        # Re-sort to maintain consistent ordering
        Q = deque(sorted(Q))
    
    if len(order) != len(D.keys()):
        print("Graph contains cycle :(")
        return None
    
    return order

r = findTopologicalOrdering(D)

print(r)

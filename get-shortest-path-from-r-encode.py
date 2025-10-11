rEncoded = {
    "A": None,
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "B",
    "F": "C"
}

def getShortestPath(encoded, s):
    if s not in encoded:
        return [None]

    path = []
    prev = encoded[s]

    while prev:
        path.append(prev)
        prev = encoded[prev]

    path.reverse()
    path.append(s)
    return path
    
print('the shortest path is: ' + str(getShortestPath(rEncoded, 't')))

rEncoded = {
    "A": None,
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "B",
    "F": "C",
    "G": "F"
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

def getLongestPath(encoded):
    max = 0

    for v in encoded:
        path = getShortestPath(encoded, v)
        dist = len(path)

        if dist > max:
            max = dist
        
    return dist

print('the longest path is: ' + str(getLongestPath(rEncoded)))

rEncoded = {
    "A": None,
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "B",
    "F": "C",
    "G": "F",
    "H": "C"
}

def getLeaves(p):
    leaves = []

    for v in p:
        if v not in p.values():
            leaves.append(v)

    return leaves

print('leaves: ' + str(getLeaves(rEncoded)))


adjacency_list={
    'A':['B','E'],
    'B':['A','C','E'],
    'C':['B','F'],
    'D':['G','H'],
    'E':['A','B','F'],
    'F':['C','E','I'],
    'G':['D','H'],
    'H':['D','G'],
    'I':'F'
}


def count_reachable_nodes(origin):
    visited = []
    return _count_reachable_nodes(origin, visited)

def _count_reachable_nodes(origin, visited):
    total = 1   #origin to origin
    visited.append(origin)
    for destination in adjacency_list[origin]:
        if destination not in visited:
            total += _count_reachable_nodes(destination, visited)
    return total

print(count_reachable_nodes('A'))
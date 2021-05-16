
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

def shortest_path(start, end):
    next_level = [start]
    visited = [start]
    distance = 0
    while next_level:
        current_level = next_level
        next_level = []
        if end in current_level:
            return distance
        for vertex in current_level:
            for destination in adjacency_list[vertex]:
                if destination not in visited:
                    visited.append(destination)
                    next_level.append(destination)
        distance += 1
    return None

print(shortest_path('A','C'))
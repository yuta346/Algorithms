adjacent_matrix={
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

#this matrix contains unconnected graph
adjacent_matrix2={
    'A':['C'],
    'B':['A','D'],
    'C':['E','F'],
    'D':['C'],
    'E':[],
    'F':[]
}
##############
#iterative dfs
##############
def bfs_iter1(start):
    visited = []
    queue = []
    queue.append(start)
    while queue:
        current = queue.pop(0)
        if current not in visited: 
            visited.append(current)
            print("Visited item:",visited)
            #print("Current stack is: ",stack)
        for neighbor in adjacent_matrix[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                print("Added neighbor is: ",queue)
bfs_iter1('A')

#########################################
#iterative dfs handles disconnected graph
#########################################
def bfs_iter2(vertex, visited):
    queue = []
    queue.append(vertex)
    while queue:
        current = queue.pop(0)
        if current not in visited: 
            visited.append(current)
            print("Visited item:",visited)
            #print("Current stack is: ",stack)
        for neighbor in adjacent_matrix[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                #print("Added neighbor is: ",stack)
def bfs_iter_driver():
    visited = []
    for vertex in list(adjacent_matrix):
        if vertex not in visited:
            bfs_iter2(vertex, visited)
#bfs_iter_driver()


##############
#Recursive dfs
##############
def bfs_recursive(start, visited):
        visited.add(start)
        print(start,end=' ')

        for neighbour in adjacent_matrix[start]:
            if neighbour not in visited:
                bfs_recursive(neighbour, visited)
def bfs_rec_driver1(start):
        visited = set()
        bfs_recursive(start, visited)
#bfs_rec_driver1('A')

#########################################
#recursive bfs handles disconnected graph
#########################################
def bfs_recursive2(start, visited):
        visited.append(start)
        print(start,end=' ')
        for neighbour in adjacent_matrix[start]:
            if neighbour not in visited:
                bfs_recursive2(neighbour, visited)
def bfs_rec_driver2():
        visited = []
        for vertex in list(adjacent_matrix):
            if vertex not in visited: 
                bfs_recursive2(vertex, visited)
#bfs_rec_driver2()

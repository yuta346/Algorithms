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
##############
#iterative dfs
##############
def dfs_iter1(start):
    visited = []
    stack = []
    stack.append(start)
    while stack:
        current = stack.pop()
        if current not in visited: #if popped item' not been visited
            visited.append(current)
            print("Visited item:",visited)
            #print("Current stack is: ",stack)
        for neighbor in adjacent_matrix[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                #print("Added neighbor is: ",stack)
#dfs_iter1('A')

#########################################
#iterative dfs handles disconnected graph
#########################################
def dfs_iter2(vertex, visited):
    stack = []
    stack.append(vertex)
    while stack:
        current = stack.pop()
        if current not in visited: #if popped item' not been visited
            visited.append(current)
            print("Visited item:",visited)
            #print("Current stack is: ",stack)
        for neighbor in adjacent_matrix[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                #print("Added neighbor is: ",stack)
def dfs_iter_driver():
    visited = []
    for vertex in list(adjacent_matrix):
        if vertex not in visited:
            dfs_iter2(vertex, visited)
#dfs_iter_driver()

##############
#Recursive dfs
##############
def dfs_recursive(start, visited):
        visited.add(start)
        print(start,end=' ')

        for neighbour in adjacent_matrix[start]:
            if neighbour not in visited:
                dfs_recursive(neighbour, visited)
def dfs_rec_driver1(start):
        visited = set()
        dfs_recursive(start, visited)
dfs_rec_driver1('A')

#########################################
#recursive dfs handles disconnected graph
#########################################
def dfs_recursive2(start, visited):
        visited.append(start)
        print(start,end=' ')
        for neighbour in adjacent_matrix[start]:
            if neighbour not in visited:
                dfs_recursive2(neighbour, visited)
def dfs_rec_driver2():
        visited = []
        for vertex in list(adjacent_matrix):
            if vertex not in visited: 
                dfs_recursive2(vertex, visited)
dfs_rec_driver2()

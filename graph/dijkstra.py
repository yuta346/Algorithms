from heapq import *
import numpy as np

graph = { 'A': {'B':1,'E':4,'F':8},
         'B': {'C':2,'F':6,'G':6},
         'C': {'D':1,'G':2},
         'D': {'H':4,'G':1},
         'E': {'F':5},
         'F':{},
         'G':{'F':1,'H':1},
         'H':{}}

def dijkstra(graph, start):
    dist = {vertex: np.inf for vertex in graph}         #distance matrix
    dist[start] = 0                                     #set A's distance to 0
    prev = {vertex:None for vertex in graph}            #prev(u)=nil

    priority_queue = []                                 #create a priority queue
    heappush(priority_queue,(0,"A"))                    #push start vertex and cost

    while priority_queue:                               #while priority queue is not empty
        current_dist, current_vertex = heappop(priority_queue)
        for neighbor, cost in graph[current_vertex].items(): #for all edges(u,v)∈ E
            if dist[neighbor]>current_dist+ cost:  
                dist[neighbor] = current_dist + cost    #update distance
                prev[neighbor] = current_vertex
                heappush(priority_queue, (current_dist + cost, neighbor)) 
                print(dist)
    print("____________________________________________________________________________________")   
    for vertex, distance in dist.items():
        print(f"Shortest path from A to {vertex} is: {distance}")
    print("____________________________________________________________________________________")
    for vertex, parent in prev.items():
        print(f"{vertex}'s parent is: {parent}")

dijkstra(graph, "A")



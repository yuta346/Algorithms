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

def bellmanFord(graph, start):
    dist = {vertex: np.inf for vertex in graph}      #distance matrix
    dist[start] = 0                                     #set A's distance to 0
    prev = {vertex:None for vertex in graph}            #prev(u)=nil

    for _ in range(len(graph)-1):
        for vertex in graph:
            print(vertex)
            for neighbor in graph[vertex]:
                if dist[neighbor] > dist[vertex] + graph[vertex][neighbor]:
                    dist[neighbor] = dist[vertex] + graph[vertex][neighbor]
                    prev[neighbor] = vertex
                    print(dist)
    print("____________________________________________________________________________________")   
    for vertex, distance in dist.items():
        print(f"Shortest path from A to {vertex} is: {distance}")
    print("____________________________________________________________________________________")
    for vertex, parent in prev.items():
        print(f"{vertex}'s parent is: {parent}")



bellmanFord(graph, "A")



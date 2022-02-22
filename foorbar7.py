import math
import numpy as np

def isLoop(a,b):
    if a == b:
        return False
    c = a + b
    while (c % 2 ==  0):
        c = c/2
    return (a % c != 0)
    
def searchMin(graph):
    keys = graph.keys()
    index = 0
    while len(graph[keys[index]]) == 0:
        index += 1
    for i in range(1,len(keys)):
        if len(graph[keys[i]]) < len(graph[keys[index]]) and len(graph[keys[i]]) > 0:
            index = i
    return keys[index]

def searchMax(graph,n):
    keys = graph.keys()
    index = 0
    while n not in graph[keys[index]]:
        index += 1
    for i in range(len(keys)):
        if n in graph[keys[i]] and len(graph[keys[i]]) < len(graph[keys[index]]):
            index = i
    return keys[index]

def deleteIndex(graph,index):
    graph.pop(index)
    for key in graph.keys():
        a = graph[key]
        if index in a:
            a.remove(index)
        if a != []:
            graph[key] = a

def solution(L):
    n = len(L)
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        for j in range(i+1,n):
            if isLoop(L[i],L[j]):
                graph[i].append(j)
                graph[j].append(i)
    C = n

    while len(set([tuple(i) for i in graph.values()])) > 1:
        index_1 = searchMin(graph)
        index_2 = searchMax(graph,  index_1)
        deleteIndex(graph, index_1)
        deleteIndex(graph,index_2)
        C -= 2
    return C

print(solution([1, 7, 3, 21, 13, 19,33,56,67,87,13123,431524,1231234,6334,123,25235,3563546]))
print(solution([1, 7, 3, 21, 13, 19]))
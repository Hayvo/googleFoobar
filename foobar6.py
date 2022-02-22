import numpy as np

def dist(pos1, pos2):
    '''Return the L1 distance between 2 positions on the grid'''
    return abs(pos2[1] - pos1[1]) + abs(pos2[0] - pos1[0])

def neighborhood(map, i, j, l_close): 
    '''Return available neighbor position'''
    l = []
    n,m = len(map),len(map[0])
    for di in [-1,1]:
       
        if (0 <= i + di) and (i+di < n) and j < m:
            print(n,i+di,j)
            if map[i+di][j] == 0 and (i+di,j) not in l_close.keys():
                l.append((i+di,j))
    for dj in [-1,1]:
        
        if (0 <= j +dj) and (j+dj < m) and i < n:
            print(m, i,j+dj)
            if map[i][j+dj] == 0 and (i,j+dj) not in l_close.keys():
                l.append((i,j+di))
    return l

def search_min(l_open): 
    '''Return the point with the best quality for the A* algorithm'''
    nodes = list(l_open.keys())
    best_node = nodes[0]
    for node in nodes:
        if l_open[node][2] < l_open[best_node][2]:
            best_node = node
    return best_node

def Astar(map, node, l_open, l_close, start, end): 
    '''Search the shortest path between start and end using A* algorithm'''
    if node != end and l_open != {}:
        neighbors = neighborhood(map, node[0], node[1], l_close)
        for new_node in neighbors:
            newG = dist(new_node, start)
            newH = dist(new_node, end)
            newF = newG + newH
            nodes_open = list(l_open.keys())
            if new_node in nodes_open:
                info = l_open[new_node]
                if newH < info[2]:
                    l_open[new_node] = [node, newG, newH, newF]
            else:
                l_open[new_node] = [node, newG, newH, newF]
        best_node = search_min(l_open)
        l_close[best_node] = l_open[best_node]
        l_open.pop(best_node)
        return Astar(map, best_node, l_open, l_close, start, end)
    else:
        node = end
        path = [end]
        while node != start:
            node = l_close[node][0]
            path.append(node)
        return path
        

def solution(map):
    for l in map:
        print(l)
    n,m = len(map),len(map[0])
    start_point = [0,0]
    end_point = [n-1,m-1]
    start = (0, 0)
    end = (n-1, m-1)
    startG = 0
    startH = dist(start, end)
    l_open = {start : [start, startG, startH, startH]}
    l_close = {}
    path = Astar(map, start, l_open, l_close, start, end)
    
    print(path)

solution([[0, 0, 0, 0, 0, 0]
        , [1, 1, 1, 1, 1, 0]
        , [0, 0, 0, 0, 0, 0]
        , [0, 1, 1, 1, 1, 1]
        , [0, 1, 1, 1, 1, 1]
        , [0, 0, 0, 0, 0, 0]])
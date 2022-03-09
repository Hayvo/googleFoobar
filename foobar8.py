import numpy as np
import sys 

sys.setrecursionlimit(10000)

def dist(pos1,pos2):
    return np.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)


def solution(dim, pos_1, pos_2, max_dist):
    def isReachable(pos):
        return dist(pos,pos_1) <= max_dist

    l,h = dim
    dx1,dx2,dy1,dy2 = l - pos_2[0], pos_2[0], pos_2[1], h - pos_2[1] 
    _dx1,_dx2,_dy1,_dy2 = l - pos_1[0], pos_1[0], pos_1[1], h - pos_1[1] 

    pos_2 = tuple(pos_2)
    pos_1 = tuple(pos_1)  
        
    if pos_1 == pos_2:
        return 0

    def explore(non_visited,visited):
        if len(non_visited) == 0:
            return list(visited.keys())
        else:
            for data in non_visited:
                pos = (data[0],data[1])
                dx1,dx2,dy1,dy2 = data[2:]
                visited[pos] = True
                non_visited.remove(data)
                new_datas = [(pos[0] + 2*dx2,pos[1])+(-dx2,-dx1,dy1,dy2),(pos[0] + 2*dx1,pos[1])+(-dx2,-dx1,dy1,dy2),(pos[0],pos[1]+2*dy2)+(dx1,dx2,-dy2,-dy1),(pos[0],pos[1]+2*dy1)+(dx1,dx2,-dy2,-dy1)]
                for new_data in new_datas:
                    new_pos = (new_data[0],new_data[1])
                    if new_pos[0] >= 0 and new_pos[1] >= 0:
                        if isReachable(new_pos) and new_pos not in visited.keys():
                            non_visited.append(new_data)

                return explore(non_visited,visited)

    trainer_pos = explore([pos_2+(dx1,-dx2,-dy1,dy2)],{})
    myself_pos = explore([pos_1+(_dx1,-_dx2,-_dy1,_dy2)],{})

    data_trainer = []
    data_myself = []

    for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        for pos in trainer_pos:
            new_pos = (dx*pos[0],dy*pos[1])
            if isReachable(new_pos):
                data_trainer.append(new_pos + tuple("t"))
        for pos in trainer_pos:
            new_pos = (dx*pos[0],dy*pos[1])
            if isReachable(new_pos):
                data_trainer.append(new_pos + tuple("t"))

    d = {}

    for data in data_trainer:
        pos = data[:2]
        theta = np.arctan2(pos[0]-pos_1[0],pos[1]-pos_1[1])
        distance = dist(pos_1,pos)
        d.setdefault(theta, []).append((distance,data[2]))
    for data in data_myself:
        pos = data[:2]
        theta = np.arctan2(pos[0]-pos_1[0],pos[1]-pos_1[1])
        distance = dist(pos_1,pos)
        d.setdefault(theta, []).append((distance,data[2]))

    def findClosest(L):
        dataMin = (10**8,'t')
        for data in L:
            if data[0] < dataMin[0]:
                dataMin = data
        return dataMin

    reachable = 0

    for key in d.keys():
        dataMin = findClosest(d[key])
        if dataMin[1] == 't':
            reachable += 1
          
    return reachable

print(solution([300,275], [150,150], [185,100], 500))

print(solution([3,2], [1,1], [2,1], 4))

print(solution([3,2], [1,1],[1,1],4))

print(solution([2,5], [1,2],[1,4],11))

print(solution([345,678],[45,67],[275,134],10000))
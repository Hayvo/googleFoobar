from turtle import pos
import numpy as np


def dist(pos1,pos2):
    return np.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)



def solution(dim, pos_1, pos_2, max_dist):

    def isReachable(pos):
        return dist(pos,pos_1) <= max_dist

    l,h = dim
    dx1,dx2,dy1,dy2 = l - pos_2[0], pos_2[0], pos_2[1], h - pos_2[1] 
    _dx1,_dx2,_dy1,_dy2 = l - pos_1[0], pos_1[0], pos_1[1], h - pos_1[1] 

    def explore(non_visited,visited,dx1,dx2,dy1,dy2):
        print(visited,non_visited)
        if len(non_visited) == 0:
            return visited.keys()
        else:
            for pos in non_visited:
                non_visited.remove(pos)
                if pos not in visited.keys():
                    visited[pos] = True
                    new_pos = [(pos[0]+dx1,pos[1]),(pos[0]+dx2,pos[1]),(pos[0],pos[1]+dy1),(pos[0],pos[1]+dy2)]
                    for n_pos in new_pos:
                        print(n_pos)
                        if isReachable(n_pos) and n_pos not in visited.keys():
                            non_visited.append(pos)
                            explore(non_visited,visited,dx1,dx2,dy1,dy2)

    pos_2 = tuple(pos_2)
    pos_1 = tuple(pos_1)
    return explore([pos_2],{},dx1,dx2,dy1,dy2)

print(solution([10,10],[1,4],[5,6],50))
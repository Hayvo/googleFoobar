from math import *


def solution(area):
    L = []
    while(area > 0):
        a = int(sqrt(area))
        L.append(a**2)
        area -= a**2
    print(*L,sep=',')

solution(15324) 
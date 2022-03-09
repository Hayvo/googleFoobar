from itertools import product
from math import atan2


def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])


    
print(solution([300,275], [150,150], [185,100], 500))

print(solution([3,2], [1,1], [2,1], 4))

print(solution([3,2], [1,1],[1,1],4))

print(solution([2,5], [1,2],[1,4],11))

print(solution([345,678],[45,67],[275,134],10000))
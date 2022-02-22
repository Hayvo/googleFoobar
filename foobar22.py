from fractions import Fraction  
def solution(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in range(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    if FirstGearRadius < 2:
        return [-1,-1]

    currentRadius = FirstGearRadius
    for index in range(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

from fractions import Fraction  

def solution(pegs):
    n = len(pegs)
    if ((not pegs) or n == 1):
        return [-1,-1]

    
    sum = (- pegs[0] + pegs[n - 1]) if (n%2==0) else (- pegs[0] - pegs[n -1])

    if (n > 2):
        for i in range(1, n-1):
            sum += 2 * (-1)**(i+1) * pegs[i]

    First = Fraction(2 * (float(sum)/(2+(-1)**n)).limit_denominator()

    if First < 2:
        return [-1,-1]

    current = First
    for i in range(0, n-2):
         
        Next = pegs[i+1] - pegs[i] - current
        if (current < 1 or Next < 1):
            return [-1,-1]
        else:
            current = Next

    return [First.numerator, First.denominator]

print(solution([4,30,50]))
print(solution([4,30,50,58]))
print(solution([0,12,23,26,41,49,70]))
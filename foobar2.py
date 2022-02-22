from fractions import Fraction

def solution(pegs):
    n = len(pegs)
    R = []
   
    r = 0
    for p in range(1,n):
        r += ((-1)**(n-1+p))*(pegs[n-p]-pegs[n-p-1])
    r = 2*r/(2+((-1)**(n%2)))
    first = r
    index = 1
    while(r>1 and index < n):
        R.append(r)
        r = pegs[index] - pegs[index-1] - r
        index += 1
    R.append(r)
    if r < 1 or first < 2:
        return [-1,-1]
    else:
        ans = Fraction(first).limit_denominator()
        return [ans.numerator,ans.denominator]

print(solution([4,30,50]))
print(solution([4,30,50,58]))
print(solution([0,12,23,26,41,49,70]))
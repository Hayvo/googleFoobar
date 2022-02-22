import numpy as np
from fractions import Fraction
from fractions import gcd


def LCMofArray(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//gcd(lcm, a[i])
    return int(lcm)

def solution(m):
    n = len(m)
    m = np.array(m, dtype = float)
    if m.shape == (1,1):
         return [1,1]
    l = n
    term = []
    not_term = []
   
    
    for i in range(n):
        s = sum(m[i])
        if s == 0:
            term.append(i)
            l -= 1
        else:
            not_term.append(i)
            for j in range(n):
                m[i,j] = m[i,j]/s

    
    not_term_mat = np.array([[m[i,j] for j in not_term] for i in not_term])
  
    term_mat = np.array([[m[i,j] for j in term] for i in not_term])
    
    res = np.dot(np.linalg.inv(np.identity(l)-not_term_mat),term_mat)[0]
    res = [Fraction(x).limit_denominator() for x in res]
    
    lcm = LCMofArray([x.denominator for x in res])
    res = [int(x.numerator * lcm / x.denominator) for x in res]
    res.append(lcm)
    
    return res

print(solution([[0, 5, 6, 0, 0, 1], 
          [4, 0, 7, 3, 2, 0], 
          [0, 1, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]))
print(solution([[0]]))
def solution(n):
    n = int(n)
    steps = 0
      
    while n > 1:
        if n & 1 == 0:
            n >>= 1
        else:
            n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)
    
        steps += 1
    return steps

print(solution('15'))
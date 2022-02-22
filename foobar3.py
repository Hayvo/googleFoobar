from re import A


def toBaseB(n,b):
    a = ''
    q = int(n)
    while q > 0:
        r = q%b
        a = str(r) + a
        q = q//b
    return a
    
def toBase10(n,b):
    a = 0
    for i,e in enumerate(n[::-1]):
        a += int(e)*b**i
    return a

def solution(n, b):
    dic = {}
    index = 1
    a =n 
    while a not in dic.keys():
        dic[a] = index
        index += 1
        a = "".join(sorted(a))
        a = toBaseB(toBase10(a[::-1],b) - toBase10(a,b),b)
    return index - dic[a]

print(solution('1211',10))
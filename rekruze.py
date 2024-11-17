def najdiMax(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] if n[0] > najdiMax(n[1:]) else najdiMax(n[1:])
    
print(najdiMax([3, 2, 6, 2]))

precalc = [0, 1]
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return precalc[-1]

    precalc.append(precalc[len(precalc) - 1] + precalc[len(precalc) - 2])
    return fib(n-1)
    
print(fib(16))

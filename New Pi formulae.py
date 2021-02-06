import sys
#Change the maximum recursion limit from 1000 to 4000 (Can be set higher for more powerful devices)
sys.setrecursionlimit(4000)
def alt_harmonic(n=0,ans=0):
    if 1/(2*n+1) < 1e-3:
        return 4 * ans
    else:
        ans += (-1)**(n) / (2*n+1)
        return alt_harmonic(n+1,ans)

def alt_harmonic_iterative():
    n = 0
    ans = 0
    while 1/(2*n+1) > 1e-5:
        ans += (-1) ** (n) / (2 * n + 1)
    return 4 * ans

print(alt_harmonic_iterative())
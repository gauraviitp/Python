import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def dfs(d, u, lp, sp):
    if lp[u] != -1:
        return None
    best = -1
    sbest = -1
    for v in d[u]:
        dfs(d, v, lp, sp)
        if sp[v] >= best:
            sbest = best
            best = sp[v]
        elif sp[v] >= sbest:
            sbest = sp[v]
    lp[u] = best + sbest + 2
    sp[u] = best + 1
    return None

def solve(d, n):
    lp = [-1] * (n + 1)
    sp = [-1] * (n + 1)
    dfs(d, 1, lp, sp)
    ma = 0
    for i in range(n + 1):
        ma = max(lp[i], sp[i], ma)
    print(ma)

def main():
    n = int(f.readline())
    d = {}
    for i in range(1, n + 1):
        d[i] = []
    for i in range(n - 1):
        u, v = map(int, f.readline().split())
        d[u].append(v)
    solve(d, n)


if __name__ == "__main__":
    main()

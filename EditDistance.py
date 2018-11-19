import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(a, b):
    na, nb = len(a), len(b)
    d = []
    for li in range(na + 1):
        d.append([0] * (nb + 1))
        for lj in range(nb + 1):
            if li == 0:
                d[li][lj] = lj
            elif lj == 0:
                d[li][lj] = li
            elif a[li - 1] == b[lj - 1]:
                d[li][lj] = d[li - 1][lj - 1]
            else:
                cd = d[li - 1][lj]
                ci = d[li][lj - 1]
                cr = d[li - 1][lj - 1]
                cm = min(ci, cd, cr) + 1
                d[li][lj] = cm
    return d[na][nb]

def main():
    t = int(f.readline())
    for _t in range(t):
        a = f.readline().rstrip()
        b = f.readline().rstrip()
        print(solve(a, b))

if __name__ == "__main__":
    main()

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

inf = int(1e10)

def solve(li, p, k):
    n = len(li)
    if n == 0:
        return (0, 0)
    li.sort()
    i = 0
    total = 0
    maxres = 0
    minres = 0 if p < li[0][0] or k > li[n - 1][0] else inf
    crimestarted = False
    while i < n:
        cur = li[i][0]

        if crimestarted and cur <= k:
            minres = min(total, minres)

        if li[i][1] == 0:
            ct = 1
            while i + 1 < n and li[i + 1][0] == cur and 0 == li[i + 1][1]:
                ct += 1
                i += 1
            total += ct
            if cur >= p and cur <= k:
                maxres = max(total, maxres)
                minres = min(total, minres)

        if li[i][1] == 1:
            ct = 1
            if cur >= p and cur <= k:
                minres = min(total, minres)
                maxres = max(total, maxres)
            while i + 1 < n and li[i + 1][0] == cur and 1 == li[i + 1][1]:
                ct += 1
                i += 1
            total -= ct
        if cur >= p:
            crimestarted = True
        i += 1

    return (minres, maxres)


def main():
    p, k = map(int, f.readline().split())
    n = int(f.readline())
    li = []
    for i in range(n):
        st, en = map(int, f.readline().split())
        li.append([st, 0])
        li.append([en, 1])
    res = solve(li, p, k)
    o.write(str(res[0]) + ' ' + str(res[1]) + '\n')

if __name__ == "__main__":
    main()

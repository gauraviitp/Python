import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def volume(cis, level):
    # b, h, w, d
    n = len(cis)
    volume = 0
    hmax = 0
    for e in cis:
        b, h, w, d = e[0], e[1], e[2], e[3]
        if level < b + h and level >= b:
            volume += (level - b) * w * d
            hmax = max(level, hmax)
        elif level >= b + h:
            volume += h * w * d
            hmax = max(b + h, hmax)
    return [volume, hmax]

def solve(cis, v):
    lo, hi = 0, int(1e6)

    vol, hmax = 0, 0
    i = 0
    while lo < hi and i < 250:
        mid = (lo + hi) / 2
        vol, hmax = volume(cis, mid)
        if abs(vol - v) <= 1e-7:
            return hmax
        elif vol > v:
            hi = mid
        else:
            lo = mid
        i += 1

    return -1 if vol < v else hmax


def main():
    t = int(f.readline())
    for tno in range(t):
        n = int(f.readline())
        cis = []
        for i in range(n):
            cis.append(list(map(int, f.readline().split())))
        v = int(f.readline())
        level = solve(cis, v)
        if level == -1:
            o.write('OVERFLOW\n')
        else:
            o.write('%.2f\n' % level)


if __name__ == "__main__":
    main()

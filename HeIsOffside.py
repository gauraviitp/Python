import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        a, d = map(int, f.readline().split())
        if a == 0 and d == 0:
            break
        aplayers = list(map(int, f.readline().split()))
        dplayers = list(map(int, f.readline().split()))

        afirst = aplayers[0]
        for i in range(1, a):
            if afirst > aplayers[i]:
                afirst = aplayers[i]

        dfirst, dsecond = min(dplayers[0], dplayers[1]), max(dplayers[0], dplayers[1])
        for i in range(2, d):
            if dfirst > dplayers[i]:
                dsecond = dfirst
                dfirst = dplayers[i]
            elif  dsecond > dplayers[i]:
                dsecond = dplayers[i]

        isOffside = True
        if afirst >= dsecond:
            isOffside = False
        elif afirst >= dfirst and afirst >= dsecond:
            isOffside = False

        o.write(('Y' if isOffside else 'N') + '\n')


if __name__ == "__main__":
    main()

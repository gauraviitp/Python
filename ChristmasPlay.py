import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

inf = int(1e10)

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())

    for tno in range(1, t + 1):
        n, k = map(int, f.readline().split())
        li = list(map(int, f.readline().split()))
        li.sort()
        st, en = 0, k - 1
        mindiff = inf
        while en < n:
            mindiff = min(li[en] - li[st], mindiff)
            st += 1
            en += 1
        o.write(str(mindiff) + '\n')

if __name__ == "__main__":
    main()

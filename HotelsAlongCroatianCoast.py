import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(li, m):
    n = len(li)
    msum, sum, st, en = 0, li[0], 0, 1
    while st < n:
        while True:
            if en <= n - 1 and sum <= m:
                sum += li[en]
                if sum <= m:
                    msum = max(sum, msum)
                en += 1
            else:
                break
        sum -= li[st]
        if sum <= m:
            msum = max(sum, msum)
        st += 1
    return msum

def main():
    n, m = map(int, f.readline().split())
    li = list(map(int, f.readline().split()))
    print(solve(li, m))

if __name__ == "__main__":
    main()

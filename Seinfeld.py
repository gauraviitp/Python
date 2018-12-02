import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def minTransforms(li, a, b):
    if li[a] == '{' and li[b] == '}':
        return 0
    elif li[a] == '}' and li[b] == '{':
        return 2
    else:
        return 1

def solve(li):
    n = len(li)
    dp = [[0 for j in range(n)] for i in range(n)]

    for k in range(1, n):
        for i in range(n - k):
            st, en = i, i + k
            val = minTransforms(li, st, st + 1) + (dp[st + 2][en] if st + 2 < n else 0)
            val = min(minTransforms(li, en - 1, en) + (dp[st][en - 2] if en - 2 >= 0 else 0), val)
            val = min(minTransforms(li, st, en) + (dp[st + 1][en - 1] if st + 1 < n and en - 1 >= 0 else 0), val)
            dp[st][en] = val

    return dp[0][n - 1]

def main():
    testno = 1
    while True:
        l = f.readline().rstrip()
        if l[0] == '-':
            break
        o.write('%d. %d\n' % (testno, solve(l)))
        testno += 1

if __name__ == "__main__":
    main()

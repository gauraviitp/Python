import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout


def solve(li):
    n = len(li)
    dp = [[li[j] if i == j else 0 for j in range(n)] for i in range(n)]
    sum = [[li[j] if i == j else 0 for j in range(n)] for i in range(n)]
    for k in range(1, n):
        for i in range(n - k):
            st, en = i, i + k
            mv = max(li[st] + dp[st + 1][en] + sum[st + 1][en], dp[st][en - 1] + sum[st][en - 1] + li[en])
            sum[st][en] = li[st] + sum[st + 1][en]
            dp[st][en] = mv
    return dp[0][n - 1]

def main():
    n = int(f.readline())
    li = list(map(int, filter(lambda line: line.strip() != '',f.readlines())))
    o.write(str(solve(li)) + '\n')


if __name__ == "__main__":
    main()

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(s, dp):
    n = len(s)
    for k in range(1, n):
        for i in range(n - k):
            st, en = i, i + k
            if s[st] == s[en]:
                dp[st][en] = dp[st + 1][en - 1]
            else:
                dp[st][en] = min(dp[st][en - 1], dp[st + 1][en]) + 1
    return dp[0][n - 1]


def main():
    t = int(f.readline())
    for _t in range(t):
        s = f.readline().rstrip()
        n = len(s)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        print(solve(s, dp))

if __name__ == "__main__":
    main()

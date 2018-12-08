import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def coef(n, k, dp):
    if k > n:
        return 0
    elif n <= 0:
        return 0
    elif k == 1:
        return n
    elif k == 0:
        return 1
    elif k == n:
        return 1
    key = (n, k)
    if key in dp:
        return dp[key]
    dp[key] = coef(n - 1, k - 1, dp) + coef(n - 1, k, dp)
    dp[(n, n - k)] = dp[key]
    return dp[key]

def solve(n, k):
    dp = {}
    return coef(n, k, dp)


def main():
    t = int(f.readline())
    for tno in range(t):
        n, k = map(int, f.readline().split())
        o.write(str(solve(n - 1, k - 1)) + '\n')

if __name__ == "__main__":
    main()

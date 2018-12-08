import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def solve(n, k):
    if n < k:
        return 0
    elif k <= 0:
        return 1

    den = 1
    k = min(k, n - k)
    dp = [i for i in range(n - k + 1, n + 1)]

    for i in range(2, k + 1):
        den *= i

    for j in range(k - 1, -1, -1):
        cdiv = gcd(dp[j], den)
        dp[j] //= cdiv
        den //= cdiv
        if den == 1:
            break

    prod = 1
    for j in range(0, k):
        prod *= dp[j]
    return prod

def main():
    t = int(f.readline())
    for tno in range(t):
        n, k = map(int, f.readline().split())
        o.write(str(solve(n - 1, k - 1)) + '\n')

if __name__ == "__main__":
    main()

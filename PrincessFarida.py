import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(c):
    n = len(c)
    if n == 0:
        return 0
    dp = [0] * n
    for i in range(n):
        pmax = 0
        for j in range(2, 4):
            if i - j >= 0:
                pmax = max(pmax, dp[i - j] + c[i])
        dp[i] = max(dp[i - 1], pmax, c[i])
    return dp[n - 1]

def main():
    t = int(f.readline())

    for _t in range(1, t + 1):
        word = f.readline()
        n = int(word)
        word = f.readline()
        if word == '':
            continue
        c = list(map(int, word.split()))
        print("Case %d: %d" % (_t, solve(c)))

if __name__ == "__main__":
    main()

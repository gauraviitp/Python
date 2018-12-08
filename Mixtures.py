import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

inf = int(1e100)


def solve(li):
    n = len(li)
    dp = [[0 for j in range(n)] for i in range(n)]
    sums = []
    for i in range(n):
        row = [0] * n
        sum = 0
        for j in range(i, n):
            sum = (sum + li[j]) % 100
            row[j] = sum
        sums.append(row)

    for k in range(1, n):
        for i in range(n - k):
            st, en = i, i + k
            val = inf
            for p in range(st, en):
                if val > dp[st][p] + dp[p + 1][en] + sums[st][p] * sums[p + 1][en]:
                    val = dp[st][p] + dp[p + 1][en] + sums[st][p] * sums[p + 1][en]
            dp[st][en] = val
    return dp[0][n - 1]


def main():
    while True:
        word = f.readline()
        if word == '' or word.strip() == '':
            break
        t = int(word)
        li = list(map(int, f.readline().split()))
        o.write(str(solve(li)) + '\n')

if __name__ == "__main__":
    main()

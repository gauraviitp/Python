import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

inf = int(1e5)

f = sys.stdin
o = sys.stdout

def bfs(li, i, j, dist, dp):
    n = len(li)
    m = len(li[0])
    if i >= 0 and i < n and j >= 0 and j < m:
        dp[i][j] = min(dist, dp[i][j])
        if i + 1 < n and dp[i + 1][j] > dist + 1:
            bfs(li, i + 1, j, dist + 1, dp)
        if i - 1 >= 0 and dp[i - 1][j] > dist + 1:
            bfs(li, i - 1, j, dist + 1, dp)
        if j + 1 < m and dp[i][j + 1] > dist + 1:
            bfs(li, i, j + 1, dist + 1, dp)
        if j - 1 >= 0 and dp[i][j - 1] > dist + 1:
            bfs(li, i, j - 1, dist + 1, dp)

def solve(li):
    n = len(li)
    m = len(li[0])
    dp = [[inf if li[i][j] == '0' else 0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if li[i][j] == '1':
                bfs(li, i, j, 0, dp)
    return dp

def printMatrix(dp):
    n = len(dp)
    m = len(dp[0])
    for i in range(n):
        for j in range(m - 1):
            o.write(str(dp[i][j]) + ' ')
        o.write(str(dp[i][m - 1]))
        o.write('\n')

def main():
    t = int(f.readline())
    tno = 0
    while tno < t:
        word = f.readline().rstrip()
        if word == '':
            continue
        n, m = map(int, word.split())
        li = []
        for i in range(n):
            row = []
            word = f.readline().rstrip()
            for c in word:
                if c.isdigit():
                    row.append(c)
            li.append(row)
        dp = solve(li)
        printMatrix(dp)
        tno += 1


if __name__ == "__main__":
    main()

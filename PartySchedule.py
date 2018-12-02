import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(wt, val, budget):
    n = len(wt)
    dp = [[0 for j in range(budget + 1)] for i in range(n)]

    # for 1st weight
    for tbudget in range(budget + 1):
        if wt[0] <= tbudget:
            dp[0][tbudget] = val[0]

    # for 2nd to nth weight
    for iwt in range(1, n):
        for tbudget in range(budget + 1):
            if wt[iwt] > tbudget:
                dp[iwt][tbudget] = dp[iwt - 1][tbudget]
            else:
                dp[iwt][tbudget] = max(dp[iwt - 1][tbudget], dp[iwt - 1][tbudget - wt[iwt]] + val[iwt])

    mVal = dp[n - 1][budget]
    tbudget = budget
    while dp[n - 1][tbudget - 1] == mVal:
        tbudget = tbudget - 1

    return {'Fun': mVal, 'Budget': tbudget}

def main():
    while True:
        word = f.readline()
        if word == '' or word.rstrip() == '':
            continue
        b, n = map(int, word.split())
        if b == 0 and n == 0:
            break

        wt = [0] * n
        val = [0] * n
        for p in range(n):
            wt[p], val[p] = map(int, f.readline().split())

        d = solve(wt, val, b)
        o.write(str(d['Budget']) + ' ' + str(d['Fun']) + '\n')

if __name__ == "__main__":
    main()

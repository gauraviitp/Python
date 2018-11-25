import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(n, ct):
    sum = 0
    while n > 0:
        mod = n % 10
        sum += mod * mod
        n = n // 10
    if sum == 1:
        return ct + 1
    elif sum >= 2 and sum <= 9:
        return -1
    else:
        return solve(sum, ct + 1)

def main():
    n = int(f.readline())
    res = solve(n, 0)
    print(res)

if __name__ == "__main__":
    main()

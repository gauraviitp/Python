import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(n, d):
    if n <= 0:
        d[0] = 0
        return 0
    if n in d:
        return d[n]
    s0 = solve(n // 2, d)
    s1 = solve(n // 3, d)
    s2 = solve(n // 4, d)
    d[n] = max(n, s0 + s1 + s2)
    return d[n]

def main():
    while True:
        word = f.readline()
        if word == '':
            break
        n = int(word)
        d = {}
        solve(n, d)
        print (d[n])

if __name__ == "__main__":
    main()

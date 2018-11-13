import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def find():
    d = {}
    for i in range(0, 10):
        l = []
        l.append(i)
        j = i
        while (j * i) % 10 != i:
            l.append((j * i) % 10)
            j = (j * i) % 10
        d[i] = l
    return d

def solve(a, b, d):
    if b == 0:
        return 1
    l = d[a % 10]
    ind = b % len(l)
    if ind == 0:
        ind = len(l)
    ind -= 1
    return l[ind]


def main():
    t = int(f.readline())
    d = find()
    for _t in range(t):
        a, b = map(int, f.readline().split())
        print(solve(a, b, d))

if __name__ == "__main__":
    main()

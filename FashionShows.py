import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())
    for _t in range(t):
        n = int(f.readline())
        x = list(map(int, f.readline().split()))
        y = list(map(int, f.readline().split()))
        x.sort()
        y.sort()
        res = 0
        for i in range(n):
            res += x[i] * y[i]
        print(res)

if __name__ == "__main__":
    main()

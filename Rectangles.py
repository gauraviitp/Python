import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    n = int(f.readline())
    res = 0
    for i in range(1, n + 1):
        t = n // i - (i - 1)
        if t > 0:
            res += t
    print(res)

if __name__ == "__main__":
    main()

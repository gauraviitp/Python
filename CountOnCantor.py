import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def find(n):
    num, den = 1, 1
    i = 1
    while i < n:
        if num == 1:
            den += 1
            i += 1
            while i < n and den > 1:
                i += 1
                den -= 1
                num += 1
        elif den == 1:
            num += 1
            i += 1
            while i < n and num > 1:
                i += 1
                num -= 1
                den += 1
    return [num, den]

def main():
    t = int(f.readline())
    for _t in range(1, t + 1):
        n = int(f.readline())
        res = list(find(n))
        print ('TERM %d IS %d/%d' % (n, res[0], res[1]))

if __name__ == "__main__":
    main()

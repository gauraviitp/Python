import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def primeFactors(n):
    s = set()

    while n > 1 and n % 2 == 0:
        if 2 not in s:
            s.add(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n > 1 and n % i == 0:
            if i not in s:
                s.add(i)
            n = n // i

    if n > 1:
        s.add(n)

    return s

def totient(n):
    s = primeFactors(n)
    val = n
    for i in s:
        val = (val * (i - 1)) // i
    return val


def main():
    t = int(f.readline())
    l = list(map(int, f.readlines()))
    for i in range(len(l)):
        n = l[i]
        res = totient(n)
        o.write(str(res) + '\n')


if __name__ == "__main__":
    main()

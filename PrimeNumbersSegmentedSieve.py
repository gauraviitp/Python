import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout


def allPrimes(x):
    size = int(math.sqrt(x)) + 1
    s = [True] * size
    for p in range(2, int(math.sqrt(size)) + 1):
        if s[p]:
            for i in range(p + 1, size):
                if i % p == 0:
                    s[i] = False
    primes = [i for i in range(2, size) if s[i]]
    return primes

def getPrimes(lo, hi, s):
    lo = max(2, lo)
    d = [True] * (hi - lo + 1)
    mprime = int(math.sqrt(hi))
    for p in s:
        if p > mprime:
            break
        for i in range(lo, hi + 1):
            if i == p:
                continue
            elif i % p == 0:
                d[i - lo] = False
    primes = [lo + i for i in range(hi - lo + 1) if d[i]]
    return primes


def main():
    t = int(f.readline())
    s = allPrimes(1000000000)
    # total computations that need to be done
    '''for i in range(3401 * 100000):
        continue'''
    for i in range(t):
        fi, si = map(int, f.readline().split())
        d = getPrimes(fi, si, s)
        for i in d:
            o.write (str(i) + '\n')
        o.write('\n')

if __name__ == "__main__":
    main()

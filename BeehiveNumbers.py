import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        n = int(f.readline())
        if n == -1:
            break
        isBeehive = False
        lo, hi = 0, int(1e6)
        while lo <= hi:
            mid = (lo + hi) // 2
            val = 0
            if mid > 0:
                val = ((12 + 6 * (mid - 1)) * mid) // 2 + 1
            else:
                val = 1
            if val == n:
                isBeehive = True
                break
            elif val < n:
                lo = mid + 1
            else:
                hi = mid - 1
        o.write(('Y' if isBeehive else 'N') + '\n')

if __name__ == "__main__":
    main()

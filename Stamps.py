import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class Int(int):
    def __lt__(self, other):
        return self > other

def main():
    t = int(f.readline())
    for _t in range(1, t + 1):
        sum, n = map(int, f.readline().split())
        s = list(map(Int, f.readline().split()))
        s.sort()
        tsum = 0
        i = 0
        possible = False
        while i < n:
            tsum += s[i]
            if tsum >= sum:
                possible = True
                break
            i += 1
        print ('Scenario #%d:' % (_t))
        if possible:
            print(i + 1)
        else:
            print('impossible')
        print()

if __name__ == "__main__":
    main()

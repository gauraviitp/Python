import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        n = int(f.readline())
        if n == -1:
            break
        l = [0] * n
        sum = 0
        for i in range(n):
            l[i] = int(f.readline())
            sum += l[i]
        if sum % n != 0:
            print(-1)
        else:
            avg = sum // n
            excess = 0
            for i in range(n):
                if l[i] > avg:
                    excess += (l[i] - avg)
            print(excess)

if __name__ == "__main__":
    main()import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        n = int(f.readline())
        if n == -1:
            break
        l = [0] * n
        sum = 0
        for i in range(n):
            l[i] = int(f.readline())
            sum += l[i]
        if sum % n != 0:
            print(-1)
        else:
            avg = sum // n
            excess = 0
            for i in range(n):
                if l[i] > avg:
                    excess += (l[i] - avg)
            print(excess)

if __name__ == "__main__":
    main()

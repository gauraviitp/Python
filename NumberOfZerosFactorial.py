import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())
    for i in range(t):
        n = int(f.readline())
        p = 5
        zeros = 0
        while p <= n:
            zeros += n // p
            p = p * 5
        print (zeros)

if __name__ == "__main__":
    main()

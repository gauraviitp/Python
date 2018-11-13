import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        n = int(f.readline())
        if n == 0:
            break
        res = n * (n + 1) * (2 * n + 1) // 6
        print (res)

if __name__ == "__main__":
    main()

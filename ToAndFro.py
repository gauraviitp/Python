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
        word = f.readline()
        res = ''
        for r in range(n):
            c = r
            i = 0
            cestep = 2 * (n - r) - 1
            costep = 2 * r + 1
            while c < len(word) and i < len(word) // n:
                res += word[c]
                if i % 2 == 0:
                    c += cestep
                else:
                    c += costep
                i += 1
        print(res)

if __name__ == "__main__":
    main()

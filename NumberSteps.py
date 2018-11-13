import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())
    for i in range(t):
        x, y = map(int, f.readline().split())
        res = None
        if x % 2 == 0:
            if y >= 0 and (y == x or y == x - 2):
                res = x + y
        else:
            if y >= 0 and (y == x or y == x - 2):
                res = x + y - 1
        if res is not None:
            print (res)
        else:
            print ('No Number')


if __name__ == "__main__":
    main()

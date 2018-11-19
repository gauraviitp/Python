import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        n = int(f.readline())
        if n == 0:
            break
        a = round((n * n) / (2 * math.pi), 2)
        print("%.2f" % a)

if __name__ == "__main__":
    main()

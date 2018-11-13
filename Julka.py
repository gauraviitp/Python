import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = 10
    for i in range(t):
        x = int(f.readline())
        y = int(f.readline())
        print ((x + y) // 2)
        print ((x - y) // 2)

if __name__ == "__main__":
    main()

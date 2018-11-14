import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())
    f.readline()
    for i in range(t):
        n = int(f.readline())
        sum = 0
        for j in range(n):
            sum += int(f.readline())
        if sum % n == 0:
            print ('YES')
        else:
            print ('NO')
        f.readline()

if __name__ == "__main__":
    main()

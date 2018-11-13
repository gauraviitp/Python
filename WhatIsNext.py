import sys

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    while True:
        a, b, c = map(int, f.readline().split())
        if a == 0 and b == 0 and c == 0:
            break
        cd0, cd1 = b - a, c - b
        if cd0 == cd1:
            print('AP ' + str(c + cd1))
            continue
        r0, r1 = b / a, c / b
        if r0 == r1:
            print('GP ' + str(int(c * r1)))

if __name__ == "__main__":
    main()

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(li):
    n = len(li)
    li.sort()

    i = 0
    while i < n:
        count = 1
        while i + 1 < n and li[i] == li[i + 1]:
            i += 1
            count += 1
        yield [li[i], str(count)]
        i += 1

def main():
    t = int(f.readline())

    for tno in range(t):
        word = f.readline()
        if word == '' or word.strip() == '':
            word = f.readline()
        n = int(word)
        li = []
        for i in range(n):
            li.append(f.readline().rstrip())
        for e in solve(li):
            o.write(e[0] + ' ' + e[1] + '\n')
        o.write('\n')



if __name__ == "__main__":
    main()

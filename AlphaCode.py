import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(word, i, l):
    n = len(word)
    if i >= n:
        return 1
    if word[i] == '0':
        return 0
    if l[i] != -1:
        return l[i]
    ct = 0
    if i <= n - 2 and word[i:i + 2] >= '10' and word[i:i + 2] <= '26':
        ct += solve(word, i + 2, l)
    ct += solve(word, i + 1, l)
    l[i] = ct
    return ct

def main():
    while True:
        word = int(f.readline())
        if word == 0:
            break
        word = str(word)
        l = [-1] * (len(word) + 1)
        print(solve(word, 0, l))


if __name__ == "__main__":
    main()

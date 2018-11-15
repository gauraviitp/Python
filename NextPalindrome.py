import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def solve(val):
    allNines = True
    for i in val:
        if i != '9':
            allNines = False
    if allNines:
        word = ['0'] * (len(val) + 1)
        word[0] = '1'
        word[len(val)] = '1'
        return word

    sz = len(val)
    if sz == 1:
        return str(int(val) + 1)

    word = list(val)

    h = sz // 2
    cor = False
    for i in range(h):
        if word[sz - 1 - i] >= word[i]:
            cor = True
        word[sz - 1 - i] = word[i]
    if not cor:
        return word

    if sz % 2 == 0:
        c = ''
        if word[h] < word[h - 1]:
            c = word[h - 1]
        else :
            c = str(int(word[h - 1]) + 1)
        word[h - 1] = c
        word[h] = c
    else:
        c = str(int(word[h]) + 1)
        word[h] = c
    return word

def main():
    t = int(f.readline())
    for _t in range(t):
        val = f.readline().rstrip()
        if val != '0':
            val = val.lstrip('0')
        if val[0] == '-':
            o.write (str(0) + '\n')
            continue
        word = ''.join(solve(val))
        o.write (word + '\n')

if __name__ == "__main__":
    main()

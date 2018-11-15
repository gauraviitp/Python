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
    corrected = False
    for i in range(h):
        if word[i] < word[sz - 1 - i]:
            corrected = False
        elif word[i] == word[sz - 1 - i]:
            pass
        else:
            corrected = True
        word[sz - 1 - i] = word[i]
    if corrected:
        return word

    if sz % 2 == 0:
        c = word[h - 1]
        if word[h - 1] > word[h]:
            word[h] = c
        else :
            i = 0
            while c == '9':
                word[h - 1 - i] = '0'
                word[h + i] = '0'
                i += 1
                c = word[h - 1 - i]
            word[h - 1 - i] = str(int(c) + 1)
            word[h + i] = str(int(c) + 1)
    else:
        i = 0
        changed = False
        c = word[h]
        if c == '9':
            word[h] = '0'
            c = word[h - 1]
            changed = True
        while c == '9':
            word[h - 1 - i] = '0'
            word[h + 1 + i] = '0'
            i += 1
            c = word[h - 1 - i]
        if not changed:
            word[h] = str(int(c) + 1)
        else:
            word[h - 1 - i] = str(int(c) + 1)
            word[h + 1 + i] = str(int(c) + 1)
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

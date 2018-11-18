import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def print(words):
    n = len(words)
    for i in range(n - 1):
        o.write(words[i] + ' ')
    o.write(words[n - 1] +  '\n')

def main():
    t = int(f.readline())
    _t = 0
    while _t < t:
        words = f.readline().strip()
        if words == '':
            continue
        words = words.split()

        sum = 0
        res = ''
        if words[4].find('machula') != -1:
            sum = str(int(words[0]) + int(words[2]))
            words[4] = sum

        elif words[2].find('machula') != -1:
            sum = str(int(words[4]) - int(words[0]))
            words[2] = sum

        else:
            sum = str(int(words[4]) - int(words[2]))
            words[0] = sum

        print(words)
        _t += 1

if __name__ == "__main__":
    main()

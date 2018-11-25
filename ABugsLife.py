import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def main():
    t = int(f.readline())
    l = f.readlines()
    ct = 0
    for _t in range(t):
        n, m = map(int, l[ct].split())
        g = [[] for i in range(n + 1)]
        isCorrect = True
        bugs = [-1] * (n + 1)
        ct += 1
        for j in range(m):
            a, b = map(int, l[ct].split())
            g[a].append(b)
            g[b].append(a)
            ct += 1

        for i in range(1, n + 1):
            for b in g[i]:
                a = i
                if not isCorrect:
                    continue
                if bugs[a] != -1 and bugs[b] != -1 and bugs[a] == bugs[b]:
                    isCorrect = False
                elif bugs[a] == -1 and bugs[b] != -1:
                    bugs[a] = 1 - bugs[b]
                elif bugs[a] != -1 and bugs[b] == -1:
                    bugs[b] = 1 - bugs[a]
                elif bugs[a] == -1 and bugs[b] == -1:
                    bugs[a] = 0
                    bugs[b] = 1

        o.write('Scenario #' + str(_t + 1) + ':\n')
        if not isCorrect:
            o.write('Suspicious bugs found!\n')
        else:
            o.write('No suspicious bugs found!\n')

if __name__ == "__main__":
    main()A

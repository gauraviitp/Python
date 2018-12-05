import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def buildTable(pattern):
    n = len(pattern)
    dp = [-1] * (n + 1)

    pos, cnd = 1, 0
    while pos < n:
        if pattern[pos] == pattern[cnd]:
            dp[pos] = dp[cnd]
        else:
            dp[pos] = cnd
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = dp[cnd]
        pos += 1
        cnd += 1
    dp[pos] = cnd
    return dp

def kmp(word, pattern):
    dp = buildTable(pattern)
    n = len(word)
    m = len(pattern)
    i, j = 0, 0
    while i < n:
        if word[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                yield i - j
                j = dp[j]
        else:
            while j >= 0 and word[i] != pattern[j]:
                j = dp[j]
            i += 1
            j += 1
    return -1

def main():
    while True:
        word = f.readline()
        if word == '':
            break
        n = int(word)
        pattern = f.readline().rstrip()
        word = f.readline().rstrip()
        for res in kmp(word, pattern):
            o.write (str(res) + '\n')
        o.write('\n')


if __name__ == "__main__":
    main()

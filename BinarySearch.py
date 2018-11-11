import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def binary_search(l, key):
    lo = 0
    hi = len(l) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            hi = mid - 1
        elif l[mid] < key:
            lo = mid + 1
    return -1

def main():
    l = [1, 2, 3, 5]
    print(binary_search(l, 2))
    print(binary_search(l, 9))

if __name__ == "__main__":
    main()

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

def main():
    t = int(f.readline())
    for i in range(t):
        n = int(f.readline())
        print (factorial(n))

if __name__ == "__main__":
    main()

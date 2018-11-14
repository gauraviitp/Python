import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

# solution is obtained by solving the below equation
# (192 + x)^3 % 1000 = 888
# It becomes clear that 1000 divides x^3 which means x has at least one 2 and one 5
# and 125 divides x which means x has at least three 5
# Thus, x has one 2 and three 5 which means x is 250

def main():
    t = int(f.readline())
    for _t in range(t):
        k = int(f.readline())
        print(192 + 250 * (k - 1))

if __name__ == "__main__":
    main()

import sys

def main():
    f = sys.stdin
    if len(sys.argv) >= 2:
        f = open(sys.argv[1])

    t = int(f.readline())
    for _t in range(t):
        M, F, N = map(int, f.readline().split())
        foods = []

        for i in range(N):
            p, s = map(int, f.readline().split())
            foods.append([p, s])
        foods.sort()

        best = 0
        for d in range(1, M // F + 1):
            money = M - d * F
            meals = 0
            can_buy = 0
            for p, s in foods:
                if p > money:
                    break
                can_buy = min(d * (s + 1) - meals, money // p)
                if can_buy >= 0:
                    meals += can_buy
                    money -= can_buy * p
            best = max(meals, best)
        print ("Case #%d: %d" % (_t + 1, best))

if __name__ == "__main__":
    main()

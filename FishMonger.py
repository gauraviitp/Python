import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

inf = int(1e10)

def djikstra(tili, toli, tt):
    n = len(tili)
    q = []
    dist = [inf] * n
    time = [inf] * n
    dist[0] = 0
    time[0] = 0
    # toll, time, node
    heapq.heappush(q, [0, 0, 0])
    res = []
    while len(q) > 0:
        node = heapq.heappop(q)
        u = node[2]
        utime = node[1]
        udist = node[0]

        if u == n - 1:
            break
        for v in range(n):
            timefromutov = utime + tili[u][v]
            distfromutov = udist + toli[u][v]
            if v != u and timefromutov <= tt:
                if distfromutov < dist[v]:
                    dist[v] = distfromutov
                    time[v] = timefromutov
                    heapq.heappush(q, [dist[v], time[v], v])
                elif timefromutov < time[v]:
                    heapq.heappush(q, [distfromutov, timefromutov, v])

    return [dist[n - 1], time[n - 1]]

def solve(tili, toli, tt):
    return djikstra(tili, toli, tt)

def main():
    while True:
        n, t = map(int, f.readline().split())
        if n == 0 and t == 0:
            break

        # tili - time list
        tili = []
        for i in range(n):
            tili.append(list(map(int, f.readline().split())))

        f.readline()

        # toli - toll list
        toli = []
        for i in range(n):
            toli.append(list(map(int, f.readline().split())))

        res = solve(tili, toli, t)
        o.write(str(res[0]) + ' ' + str(res[1]) + '\n')
        f.readline()

if __name__ == "__main__":
    main()

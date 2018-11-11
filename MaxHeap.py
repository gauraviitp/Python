import sys
import queue

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

f = sys.stdin
o = sys.stdout

class MyInt(int):

    def __lt__(self, other):
        return self > other

def main():
    q = queue.PriorityQueue()
    q.put(MyInt(10))
    q.put(MyInt(5))
    q.put(MyInt(1))
    while not q.empty():
        print (q.get())


if __name__ == "__main__":
    main()
